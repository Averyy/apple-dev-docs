# Web Inspector

**Framework**: Safari Developer Features

Use Web Inspector to inspect and debug your HTML, CSS, and JavaScript.

#### Overview

Web Inspector helps you inspect all the resources and activity on webpages, service workers, Mac and Home Screen web apps, and JavaScript running inside your applications, making development more efficient across Apple platforms. The clean, unified design puts each core function in a separate tab, which you can rearrange to fit your workflow.

The most complete resource for Web Inspector is the [`Web Inspector Reference`](https://developer.apple.comhttps://webkit.org/web-inspector/), and help links in Web Inspector itself can take you to help specific to the current part of the tools you are using.

#### The Interface

Web Inspector is divided into multiple tabs, with navigation and details sidebars, a main content area, a console prompt at the bottom, and optionally a split console visible in every tab. Learn more about [`Web Inspector’s interface`](https://developer.apple.comhttps://webkit.org/web-inspector/web-inspector-interface/) as well as how to quickly navigate Web Inspector with [`keyboard shortcuts`](https://developer.apple.comhttps://webkit.org/web-inspector/keyboard-shortcuts/).

![Overview of Web Inspector’s interface, with a tab bar at the top, a navigation sidebar, content area, and details sidebar in the middle, and the console prompt at the bottom.](https://docs-assets.developer.apple.com/published/6c979bb3ac204dbb2b08e5fe161c697a/WebInspector-Interface~dark%402x.png)

Each tab contains a set of related tools and features to make it easier to find the tool you are looking for.

- **[`Elements`](https://developer.apple.comhttps://webkit.org/web-inspector/elements-tab/)**: View and inspect the elements that make up the DOM of a webpage. Clicking elements from the fully editable markup tree on the left reveals the node’s styles in the middle sidebar, with more details in the right sidebar.
- **[`Console`](https://developer.apple.comhttps://webkit.org/web-inspector/console-command-line-api/)**: Type JavaScript commands in the console to interactively debug, modify, and get information about your webpage. View logs, errors, and warnings emitted from a webpage, so you can identify issues fast and resolve them right away.
- **[`Sources`](https://developer.apple.comhttps://webkit.org/web-inspector/sources-tab/)**: Find every resource of a webpage, including documents, images, scripts, stylesheets, and more. Use the built-in debugger with data type and code highlights to troubleshoot and understand the script execution flow.
- **[`Network`](https://developer.apple.comhttps://webkit.org/web-inspector/network-tab/)**: See a detailed list of all network requests made to load every webpage resource, so you can quickly evaluate the response, status, timing, and more.
- **[`Timelines`](https://developer.apple.comhttps://webkit.org/web-inspector/timelines-tab/)**: Understand all the activity that occurs on an open webpage, such as network requests, layout and rendering, JavaScript events, memory, and CPU impact. Everything is neatly plotted on a timeline or recorded by frame, helping you discover ways to optimize your site.
- **[`Web Inspector Reference`](https://developer.apple.comhttps://webkit.org/web-inspector/)**: Find details about the data stored by a webpage, such as application cache, cookies, databases, indexed databases, local storage, and session storage.
- **[`Web Inspector Reference`](https://developer.apple.comhttps://webkit.org/web-inspector/)**: Preview animation keyframes and their classes from HTML5 canvas, JavaScript animations, CSS animations, and CSS transitions. Dial in the motion and the visual design of webpages.
- **[`Layers`](https://developer.apple.comhttps://webkit.org/web-inspector/layers-tab/)**: Visualize compositing layers in 3D to understand where layers are generated and in what order they’ll render. Use layers to help find unexpected memory consumption or excessive repaints on a webpage.
- **[`Audit`](https://developer.apple.comhttps://webkit.org/web-inspector/audit-tab/)**: Preform audits against a webpage to certify that common code and accessibility errors are addressed. Confirm that a webpage follows design guidelines and specifications of modern webpages.

## See Also

- [Develop menu](develop-menu.md)
  Access tools for debugging webpages in Safari, as well as tools for debugging web content in other apps and on other devices.
- [Responsive Design Mode](responsive-design-mode.md)
  Use Responsive Design Mode to test your `media` queries and other dynamic styles to ensure your webpages look great on any screen.
- [Inspect Apps and Devices](inspect-apps-and-devices.md)
  Discover all inspectable web content in Safari and other apps on your Mac and on connected devices.
- [Connecting an AI agent to Safari](connecting-an-ai-agent-to-safari.md)
  Inspect, test, and debug your website with an AI agent connected to the Safari MCP server.
- [WebDriver](webdriver.md)
  Use WebDriver to write robust, comprehensive tests and run them against any browser that has a WebDriver-compliant driver, including Safari.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-developer-tools/web-inspector)*