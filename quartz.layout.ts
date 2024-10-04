import { PageLayout, SharedLayout } from "./quartz/cfg";
import * as Component from "./quartz/components";
import { IconFolderOptions } from "./quartz/plugins/components/FileIcons";
import { filterFn, sortFn } from "./quartz/util/function";

// components shared across all pages

const iconsOptions: IconFolderOptions = {
	rootIconFolder: "quartz/static/icons",
	default: {
		file: "file",
	},
};

export const secretPage = new Set(["hidden"]);

export const sharedPageComponents: SharedLayout = {
	head: Component.Head(),
	afterBody: [],
	header: [
		Component.MobileOnly(
			Component.ExplorerBurger({
				folderDefaultState: "open",
				folderClickBehavior: "link",
				iconSettings: iconsOptions,
				sortFn,
				filterFn,
			}),
		),
		Component.MobileOnly(Component.PageTitle()),
		Component.MobileOnly(Component.Spacer()),
		Component.Search(),
		Component.Darkmode(),
	],
	footer: Component.Footer({
		links: {
			Github: "https://github.com/Enveloppe/obsidian-enveloppe",
			Discussion: "https://github.com/orgs/Enveloppe/discussions",
			Discord: "https://discord.gg/6DyY779Nbn",
		},
	}),
};

// components for pages that display a single page (e.g. a single note)
export const defaultContentPageLayout: PageLayout = {
	beforeBody: [
		Component.Breadcrumbs(),
		Component.ArticleTitle(iconsOptions),
		Component.ContentMeta({ showReadingTime: false }),
		Component.TagList(),
	],
	left: [
		Component.DesktopOnly(Component.PageTitle()),
		Component.DesktopOnly(
			Component.ExplorerBurger({
				folderClickBehavior: "link",
				folderDefaultState: "collapsed",
				useSavedState: true,
				title: "",
				iconSettings: iconsOptions,
				sortFn,
				filterFn,
			}),
		),
	],
	right: [
		Component.DesktopOnly(Component.Graph()),
		Component.DesktopOnly(Component.TableOfContents()),
		Component.DesktopOnly(Component.Backlinks()),
	],
};

// components for pages that display lists of pages  (e.g. tags or folders)
export const defaultListPageLayout: PageLayout = defaultContentPageLayout;
