# Xcode 26.3 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

Xcode 26.3 includes Swift 6.2.3 and SDKs for iOS 26.2, iPadOS 26.2, tvOS 26.2, macOS 26.2, and visionOS 26.2. Xcode 26.3 supports on-device debugging in iOS 15 and later, tvOS 15 and later, watchOS 8 and later, and visionOS. Xcode 26.3 requires a Mac running macOS Sequoia 15.6 or later.

##### Coding Intelligence

###### New Features

- Xcode 26.3 introduces support for agentic coding, a new way in Xcode for developers to build apps, powered by coding agents from Anthropic and OpenAI. With agentic coding, Xcode can work autonomously toward a developer’s goals — from breaking down tasks to making decisions based on the project architecture, and using built-in tools to get things done. In addition to Anthropic’s Claude Agent and OpenAI’s Codex integrations, Xcode 26.3 makes its capabilities available through the Model Context Protocol, an open standard that gives developers the flexibility to use any compatible agent or tool with Xcode. For more information, see [`Setting up coding intelligence`](https://developer.apple.com/documentation/Xcode/setting-up-coding-intelligence).  (169448160)
- Xcode 26.3 introduces a comprehensive permissions system that gives you fine-grained control over what external agentic coding tools can do in your development environment.  (170740647)

###### Resolved Issues

- Fixed: The coding tools activity indicator bar no longer spontaneously appears in editors after a task has finished.  (163070450)
- Fixed an issue that caused custom model providers to disappear in between launches of Xcode.  (165930715) (FB21270045)
- Fixed: Added confirmation dialog when reverting code changes that would affect both model and manual edits.  (168171565)
- Fixed: Running code snippets with agents no longer causes subsequent build failures.  (168263181)
- Fixed “Allow All” functionality to properly handle bash commands with arguments.  (168534701)
- Fixed: Visual and performance improvements to the prompt input field.  (168706984)
- Fixed: “Allow agents to use integrated internet access tools” toggle only applies to Codex  (169237379)
- Fixed crash that could happen when invoking “Generate a Fix” via Issues Navigator.  (169309185)
- Fixed issue where externally configured MCP servers were being overwritten during Codex initialization.  (169570663)
- Fixed: Saved conversations could be lost or have some properties lost on restore.  (169997457)
- Fixed: Stopping transcript execution now properly clears queued commands.  (170094773)
- Fixed: Tool result updates for permission denials are now correctly classified as cancelled.  (170351655)
- Fixed: Resolved agent indicator not showing if Claude CLI was launched before opening a project.  (170492975)
- Fixed an issue causing Test Tools to never return any value.  (170496650)
- Fixed: JPEG images now send correctly without error messages.  (170514200)
- Fixed: Added support for Claude 4.6.  (170562239)
- Fixed OpenCode compatibility for accepting MCP responses from Xcode.  (170565579)
- Fixed: Upgraded to Codex version 0.98.0 for improved stability and features.  (170586680)
- Fixed: When using external development tools that connect to Xcode, you may see multiple “Allow Connection?” dialogs during normal usage.  (170721057)

###### Known Issues

- Denying Claude or Codex access to a project located in a privacy-protected directory - such as Desktop, Downloads, or Documents - will mean the project cannot be accessed by the agent as no subsequent access request is made and the decision cannot be reversed.  (166387271) **Workaround:** If Claude or Codex appear in the Privacy and Security -> Files and Folders section in System Settings, you can enable access there. If no entry exists, please move your project folder to a new location outside of Desktop, Downloads, or Documents before proceeding.
- Pasting files into the coding assistant UI does not consistently send their contents to agents.  (167657446) **Workaround:** Move the file to a known location, like the Desktop or your project’s working directory, and tell the agent that a file has been placed there for it to access.
- Labels in conversation history created by use of coding tools may sometimes suggest that models have changed more lines of code than they actually have.  (168022670)
- Choosing “Clear Recents” from the coding assistant’s conversation list may not clear the list.  (168096005)
- When automatic change application is disabled in the coding assistant, the undo button may not appear after you have applied a proposed change.   (168310593) **Workaround:** Use the history view or other tools like git to revert the change.
- Custom slash commands and skills can be rejected by agents when directly invoked by “/skill”.  (169214412) **Workaround:** Ask for the skill without using a slash: ‘use the `{skill-name}` skill’
- Some agent settings, such as turning on/off provider-specific telemetry or disallowing integrated web tools, may not be immediately respected by all agents.   (169316968) **Workaround:** Relaunch Xcode after changing these settings.
- MCP clients that attempt to connect to Xcode when external MCP connections are turned off can still appear as active or inactive connections in Xcode’s UI. These clients remain blocked from accessing Xcode.  (169542597)

## See Also

- [Xcode 26.4 Release Notes](xcode-26_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
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