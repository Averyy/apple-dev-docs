# Giving external agents access to Xcode

**Framework**: Xcode

Let agents access your project and Xcode capabilities using the Model Context Protocol.

#### Overview

You can give permission for external agents, that you launch outside of Xcode, to modify your Xcode project and perform actions, such as building your app.

If you use an external agent for development:

1. Allow the agent access to Xcode in Intelligence settings.
2. Configure the agent to access Xcode capabilities through the Model Context Protocol (MCP) server that Xcode provides.
3. Open your project in Xcode and begin prompting the external agent that utilizes Xcode.

Xcode alerts you when the external agent connects to Xcode and when it’s active.

##### Update Intelligence Settings to Give External Agents Access to Xcode

In Intelligence settings, allow external agents to connect with Xcode using its MCP server:

1. Choose Xcode > Settings and select Intelligence in the sidebar.
2. Under Model Context Protocol, turn on “Allow external agents to use Xcode tools.”

![A screenshot of the Intelligence settings showing the “Allow external agents to use Xcode tools” toggle under Model Context Protocol.](https://docs-assets.developer.apple.com/published/c929c7d8597d928bc77b7ebe389c7910/intelligence-settings%402x.png)

##### Configure External Agents to Use the Mcp Server

In Terminal, use the `xcrun mcpbridge` command to configure the external agent to use Xcode Tools. For example, run the following command in Terminal to give Claude Code access to your open project and Xcode capabilities:

```None
claude mcp add --transport stdio xcode -- xcrun mcpbridge
```

For Codex, run:

```None
codex mcp add xcode -- xcrun mcpbridge
```

To verify the configuration, enter `claude mcp list` or `codex mcp list` in Terminal.

Optionally, add hints about Xcode and your project to configuration files, such as the `AGENTS.md` or `CLAUDE.md` files, in the location that the external agent uses. For more information on configuring agents that run inside Xcode, see doc:setting-up-coding-intelligence#Customize-the-Codex-and-Claude-Agent-environments.

Before prompting an external agent (outside of Xcode), be sure to open your project in Xcode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/giving-external-agents-access-to-xcode)*