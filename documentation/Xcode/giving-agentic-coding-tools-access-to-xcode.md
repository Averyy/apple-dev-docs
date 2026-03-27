# Giving external agentic coding tools access to Xcode

**Framework**: Xcode

Let agentic coding tools access your project and Xcode capabilities using the Model Context Protocol.

#### Overview

You can give permission for another agentic coding tool to modify your Xcode project and perform actions, such as building your app.

First, let Xcode know in settings that you plan to use an external third-party agentic coding tool for development. Then configure the agentic coding tool to access Xcode capabilities through the Model Context Protocol (MCP) server that Xcode provides. Open your project in Xcode and begin entering prompts in the agentic coding tool that utilizes Xcode. Xcode alerts you when the external agent connects to Xcode and when it’s active.

##### Update Intelligence Settings to Give External Agents Access to Xcode

In Intelligence settings, allow external third-party agentic coding tools to connect with Xcode using its MCP server:

1. Choose Xcode > Settings and select Intelligence in the sidebar.
2. Under Model Context Protocol, toggle “Allow external agents to use Xcode tools” on.

![A screenshot of the Intelligence settings showing the “Allow external agents to use Xcode tools” toggle under Model Context Protocol.](https://docs-assets.developer.apple.com/published/bb5b02211e540f5d0602eaa21f5262a2/intelligence-settings%402x.png)

##### Configure External Coding Tools to Use the Mcp Server

In Terminal, use the `xcrun mcpbridge` command to configure the agentic coding tool to use Xcode Tools. For example, run the following command in Terminal to give Claude Code access to your open project and Xcode capabilities:

```None
claude mcp add --transport stdio xcode -- xcrun mcpbridge
```

For Codex, run:

```None
codex mcp add xcode -- xcrun mcpbridge
```

To verify the configuration, enter `claude mcp list` or `codex mcp list` in Terminal.

Optionally, add hints about Xcode and your project to configuration files, such as the `AGENTS.md` or `CLAUDE.md` files, in the location that the agentic coding tool uses. For more information on configuring agentic coding tools that run inside Xcode, see [`Customize the Codex and Claude Agent environments`](setting-up-coding-intelligence#Customize-the-Codex-and-Claude-Agent-environments.md).

Before entering prompts in the agentic coding tool outside of Xcode, be sure to open your project in Xcode.

## See Also

- [Setting up coding intelligence](setting-up-coding-intelligence.md)
  Enable third-party coding tools that you want to use in the coding assistant.
- [Writing code with intelligence in Xcode](writing-code-with-intelligence-in-xcode.md)
  Generate code, fix bugs fast, and learn as you go with intelligence built directly into Xcode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/giving-agentic-coding-tools-access-to-xcode)*