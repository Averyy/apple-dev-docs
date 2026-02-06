# Xcode 26.3 RC Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

Xcode 26.3 RC includes Swift 6.2.3 and SDKs for iOS 26.2, iPadOS 26.2, tvOS 26.2, macOS 26.2, and visionOS 26.2. Xcode 26.3 RC supports on-device debugging in iOS 15 and later, tvOS 15 and later, watchOS 8 and later, and visionOS. Xcode 26.3 RC requires a Mac running macOS Sequoia 15.6 or later.

##### Coding Intelligence

###### New Features

- Xcode 26.3 introduces support for agentic coding, a new way in Xcode for developers to build apps, powered by coding agents from Anthropic and OpenAI. With agentic coding, Xcode can work autonomously toward a developer’s goals — from breaking down tasks to making decisions based on the project architecture, and using built-in tools to get things done. In addition to Anthropic’s Claude Agent and OpenAI’s Codex integrations, Xcode 26.3 makes its capabilities available through the Model Context Protocol, an open standard that gives developers the flexibility to use any compatible agent or tool with Xcode. For more information, see [`Setting up coding intelligence`](https://developer.apple.com/documentation/Xcode/setting-up-coding-intelligence).  (169448160)

###### Resolved Issues

- Fixed: The coding tools activity indicator bar no longer spontaneously appears in editors after a task has finished.  (163070450)
- Fixed an issue that caused custom model providers to disappear in between launches of Xcode.  (165930715) (FB21270045)

###### Known Issues

- Denying Claude or Codex access to a project located in a privacy-protected directory - such as Desktop, Downloads, or Documents - will mean the project cannot be accessed by the agent as no subsequent access request is made and the decision cannot be reversed.  (166387271)  If Claude or Codex appear in the Privacy and Security -> Files and Folders section in System Settings, you can enable access there. If no entry exists please move your project folder to a new location outside of Desktop, Downloads, or Documents before proceeding.
- Pasting files into the coding assistant UI does not consistently send their contents to agents.  (167657446)  Move the file to a known location, like the Desktop or your project’s working directory, and tell the agent that a file has been placed there for it to access.
- Labels in conversation history created by use of coding tools may sometimes suggest that models have changed more lines of code than they actually have.  (168022670)
- Choosing “Clear Recents” from the coding assistant’s conversation list may not clear the list.  (168096005)
- Sometimes #Preview or #Playground executions may fail after the “Run snippet” tool runs.  (168263181)  Build the active scheme to clear up the error.
- When automatic change application is disabled in the coding assistant, the undo button may not appear after you have applied a proposed change.   (168310593)  Use the history view or other tools like git to revert the change.
- If an agent download fails, you may not be notified with error details.  (169206550)
- Custom slash commands and skills can be rejected by agents when directly invoked by “/skill”.  (169214412)  Ask for the skill without using a slash: ‘use the `{skill-name}` skill’
- “Allow agents to use integrated internet access tools” toggle only applies to Codex  (169237379)  When interacting with Claude Agent, manually allow each web-based command or allow all commands
- In some cases, ‘Generate fix for issue’ might cause Xcode to crash.  (169309185)
- Some agent settings, such as turning on/off provider-specific telemetry or disallowing integrated web tools, may not be immediately respected by all agents.   (169316968)  Relaunch Xcode after changing these settings.
- MCP clients that attempt to connect to Xcode when external MCP connections are turned off can still appear as active or inactive connections in Xcode’s UI. These clients remain blocked from accessing Xcode.  (169542597)

## See Also

- [Xcode 26.2 Release Notes](xcode-26_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 26.1.1 Release Notes](xcode-26_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 26.0.1 Release Notes](xcode-26_0_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 26 Release Notes](xcode-26-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-26_3-release-notes)*