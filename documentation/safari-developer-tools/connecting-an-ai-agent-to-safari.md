# Connecting an AI agent to Safari

**Framework**: Safari Developer Features

Inspect, test, and debug your website with an AI agent connected to the Safari MCP server.

#### Overview

Safari 27 and later includes a Model Context Protocol (MCP) server, which lets you connect an AI agent to a set of tools that inspect and interact with your pages. These tools can open tabs, load pages, read the Document Object Model (DOM), capture screenshots, monitor console and network activity, and simulate clicks, taps, and keystrokes in an active webpage.

After you connect your AI agent to the Safari MCP server, you can ask the agent to perform common development tasks such as:

- Reviewing how your page behaves in Safari for compatibility testing
- Analyzing your page’s performance
- Confirming your page’s accessibility support
- Testing your page’s interactions

#### Enable Web Developer Features and Remote Automation

Before you connect your AI agent, enable web developer features and remote automation in Safari. First, follow the steps in [`Enabling features for web developers`](enabling-developer-features.md) to enable the Develop menu and Developer settings tab.

Then, enable remote automation so that your AI agent can connect to the MCP server:

1. Choose Safari > Settings.
2. Select the Developer tab.
3. Check the “Allow remote automation and external agents” box.

#### Configure an Ai Agent to Use the Safari Mcp Server

After you enable remote automation and external agent access in Safari, you can configure your AI agent to connect to the Safari MCP server.

In Claude Code, use the command `claude mcp add` to add the Safari MCP server configuration. Provide a name for the server, such as “`safari-mcp`”, and provide the path to the `safaridriver` binary inside the Safari application bundle with the `--mcp` flag:

```bash
    
claude mcp add safari-mcp -- "/usr/bin/safaridriver" --mcp

```

In Codex, use the command `codex mcp add` to add the Safari MCP server configuration. Provide a name for the server, such as “`safari-mcp`”, and provide the path to the `safaridriver` binary inside the Safari application bundle with the `--mcp` flag:

```bash
    
codex mcp add safari-mcp -- "/usr/bin/safaridriver" --mcp

```

If your agent uses an `mcp.json` or `config.json` file, add the Safari MCP server configuration with an entry that names the command and its arguments directly, as in the following example:

```json
    
{
  "mcpServers": {
    "safari-mcp": {
      "command": "/usr/bin/safaridriver",
      "args": ["--mcp"]
    }
  }
}
    
```

#### Navigate to a Webpage with a Prompt

Start by writing a prompt that specifies a URL and the action you want to perform; for example, “Open my site at example.com in Safari and tell me if it loaded correctly.” The agent uses the Safari MCP server to open a new window in Safari and load the site you request in that window, and then uses the MCP server’s tools to see if the webpage loaded correctly. Safari displays a banner below the top toolbar that indicates your AI agent controls the window.

After the webpage opens in the window and the agent verifies it loaded correctly, the agent responds with a message similar to this example:

```None
    
I opened example.com in Safari. The page loaded successfully with a 200 response and the title "Example Domain." No console errors were reported.

```

If you request actions in your first prompt before navigating to a webpage and opening the window that the agent controls, such as listing open tabs or opening a new tab, the Safari MCP server may return an error.

#### Interact with Webpages in Safari Using the Mcp Server Tools

As you’re building and maintaining your webpages, you can ask your AI agent to interact with, test, and analyze your webpages in Safari. The MCP server provides tools that let your agent perform these types of actions:

- Open a new tab, list open tabs, switch between tabs, and close a tab.
- Navigate to a URL, wait for a webpage to finish loading, and provide basic page information such as title and load status.
- Inspect rendered page content, take a screenshot, list network requests from the page, and review console messages.
- Set a viewport size, switch to the light or dark appearance, and view the page with reduced motion.
- Test clicks, typing, scrolling, hovering, and pressing keys.
- Run JavaScript in the page’s context.
- Accept or dismiss browser dialogs.

The following table lists the tools that the Safari MCP server provides:

| Tool | Description |
| --- | --- |
| `browser_console_messages` | Returns buffered console logs for the current or specified tab |
| `browser_dialogs` | Lists and responds to browser dialogs (accepts, dismisses, or inputs text for JS prompts) |
| `close_tab` | Closes a browser tab by its handle |
| `create_tab` | Creates a new browser tab, optionally loading a URL |
| `evaluate_javascript` | Runs JavaScript code within the page and returns the result |
| `get_network_request` | Gets full detail for a single recorded network request (like headers, body, and timing) |
| `get_page_content` | Extracts text content of a page in various formats (Markdown, HTML, and JSON) |
| `list_network_requests` | Lists network request summaries (like URL, method, status, and timing) for the current tab |
| `list_tabs` | Lists all open browser tabs with their handles and URLs |
| `navigate_to_url` | Navigates to a URL and returns the loaded page’s content |
| `page_info` | Gets information about the current page: URL, title, and loading state |
| `page_interactions` | Performs DOM interactions in sequence, such as click, type, scroll, hover, and key press |
| `screenshot` | Captures a screenshot of the current page as a PNG |
| `set_emulated_media` | Emulates a CSS media type (like “print”) for responsive-design testing |
| `set_viewport_size` | Sets the browser viewport size in CSS pixels |
| `switch_tab` | Switches to a different browser tab by its handle |
| `wait_for_navigation` | Waits for the current page to finish loading, then returns the final URL and title |

## See Also

- [Develop menu](develop-menu.md)
  Access tools for debugging webpages in Safari, as well as tools for debugging web content in other apps and on other devices.
- [Web Inspector](web-inspector.md)
  Use Web Inspector to inspect and debug your HTML, CSS, and JavaScript.
- [Responsive Design Mode](responsive-design-mode.md)
  Use Responsive Design Mode to test your `media` queries and other dynamic styles to ensure your webpages look great on any screen.
- [Inspect Apps and Devices](inspect-apps-and-devices.md)
  Discover all inspectable web content in Safari and other apps on your Mac and on connected devices.
- [WebDriver](webdriver.md)
  Use WebDriver to write robust, comprehensive tests and run them against any browser that has a WebDriver-compliant driver, including Safari.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-developer-tools/connecting-an-ai-agent-to-safari)*