import argparse
from pathlib import Path
from string import Template

from pydantic import BaseModel
from git import Repo
import re
from rich.console import Console
from rich.panel import Panel
from rich.text import Text


class TemplateModel(BaseModel):
    site_name: str
    site_url: str
    site_description: str
    site_author: str
    language: str
    auto_h1: bool
    comments: bool
    submodule: bool = False

class Environment(BaseModel):
    env: str
    deploy: str


def get_git_info(repo_path="."):
    try:
        repo = Repo(repo_path)
        remote_url = repo.remotes.origin.url
        match = re.search(r"(?:https://|git@)github\.com[:/](.+?)/(.+?)(?:\.git)?$", remote_url)
        if match:
            return match.group(1), match.group(2)
        else:
            return None, None
    except Exception as e:
        print(e)
        return None, None

def create_default_page(user: str|None, repo: str|None) -> str:
    if repo == f"{user}.github.io":
        return f"https://{repo}/"
    if user and repo:
        return f"https://{user}.github.io/{repo}/"
    if user:
        return f"https://{user}.github.io/"
    return "https://example.com/"

def dry_run_template(console: Console, args: argparse.Namespace) -> None:
    if args.dry_run:
        # Titre principal
        positional_args = (
            f"- [u]site_name[/u]: {args.site_name}\n"
            f"- [u]site_url[/u]: {args.site_url}\n"
            f"- [u]site_description[/u]: {args.site_description}\n"
            f"- [u]site_author[/u]: {args.site_author}\n"
            f"- [u]language[/u]: {args.language}"
        )

        positional_panel = Panel(positional_args, title="[bold cyan]Positional Arguments[/bold cyan]", border_style="cyan")

        # Options
        options_args = (
            f"- [u]auto_h1[/u]: {args.auto_h1}\n"
            f"- [u]comments[/u]: {args.comments}\n"
            f"- [u]submodule[/u]: {args.submodule}"
        )

        options_panel = Panel(options_args, title="[bold cyan]Options[/bold cyan]", border_style="cyan")

        # Display panels
        console.print("[bold underline]Dry Run Arguments[/bold underline]")
        console.print(positional_panel)
        console.print(options_panel)

def default_args(args: argparse.Namespace, repo: str|None, user: str|None):
    default_repo_url = create_default_page(user, repo).lower()
    site_url = args.site_url
    site_name = args.site_name
    site_author = args.site_author
    if not site_url:
        site_url = default_repo_url
    if len(site_url.strip()) == 0:
        site_url = default_repo_url

    if len(site_name.strip()) == 0:
        site_name = repo if repo else user if user else "My Site"
    if len(site_author.strip()) == 0:
        site_author = user if user else repo if repo else "My Name"

    return site_url, site_name, site_author

def main() -> None:
    console = Console()
    user, repo = get_git_info()
    default_repo_url = create_default_page(user, repo).lower()
    parser = argparse.ArgumentParser(
        description="Generate a template for Obsidian Publisher"
    )
    parser.add_argument("site_name", type=str, help="The name of the site")
    parser.add_argument("site_url", type=str, help="The url of the site. If empty, will be set to: " + default_repo_url)
    parser.add_argument(
        "site_description", type=str, help="The description of the site"
    )
    parser.add_argument("site_author", type=str, help="The author of the site")
    parser.add_argument("language", type=str, help="The language of the site")
    parser.add_argument(
        "--auto-h1", action="store_true", help="Automatically add h1 to the title"
    )
    parser.add_argument(
        "--comments", action="store_true", help="Enable comments on the site"
    )
    parser.add_argument(
        "--submodule", action="store_true", help="Enable submodule for the site, for the workflow that deploy the site.")
    parser.add_argument("--dry-run", action="store_true", help="Only print the result, and not write to the file")
    args = parser.parse_args()

    args.site_url, args.site_name, args.site_author = default_args(args, repo, user)

    dry_run_template(console, args)

    template = TemplateModel(
        site_name=args.site_name,
        site_url=args.site_url if args.site_url.startswith("https://") else f"https://{args.site_url}",
        site_description=args.site_description,
        site_author=args.site_author,
        language=args.language,
        auto_h1=args.auto_h1,
        comments=args.comments,
        submodule=args.submodule if args.submodule else False
    )


    # download the files
    
    mkdocs_yaml = Path("mkdocs.yml")
    with mkdocs_yaml.open("r", encoding="UTF-8") as f:
        mkdocs = f.read()
    mkdocs = Template(mkdocs)
    s = mkdocs.substitute(
        site_name=template.site_name,
        site_url=template.site_url,
        site_description=template.site_description,
        site_author=template.site_author,
        language=template.language,
        auto_h1=template.auto_h1,
        comments=template.comments,
    )
    if not args.dry_run:
        with mkdocs_yaml.open("w", encoding="UTF-8") as f:
            f.write(s)
    # panel
    mkdocs_generated_panel = Panel(Text(s), title="[bold cyan]mkdocs.yml[/bold cyan]", border_style="cyan")
    console.print(mkdocs_generated_panel)


    if template.submodule:
        workflow_path = Path(".github/workflows/deploy.yml")
        with workflow_path.open("r", encoding="UTF-8") as f:
            workflow = f.read()
        wf=workflow.replace("FETCH_SUBMODULE: false", "FETCH_SUBMODULE: true")
        if not args.dry_run:
            with workflow_path.open("w", encoding="UTF-8") as f:
                f.write(wf)
        # panel
        workflow_generated_panel = Panel(Text(wf), title="[bold cyan]deploy.yml[/bold cyan]", border_style="cyan")
        console.print(workflow_generated_panel)

    console.print("[bold green]Template generated successfully![/bold green]")

if __name__ == "__main__":
    main()