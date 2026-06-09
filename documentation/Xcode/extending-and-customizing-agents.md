# Extending and customizing agents

**Framework**: Xcode

Expand agent capabilities for your specific needs and application domain.

#### Overview

You can give agents more guidance and expertise so that they work productively, can validate their own work, and operate autonomously on your tasks with less intervention. To do this, grant agents permission to use system commands and tools, request agents use built-in skills, add agent-specific configuration files, and install external plug-ins that add more capabilities.

#### Control Access to External Commands and Tools

If you want finer control over agents using commands and tools while performing tasks, you can grant or deny access in Intelligence settings.

To manage these permissions, click the Permissions row under Agents in Xcode. Any commands or tools that you previously granted access to in the coding assistant appear here.

To give access to a command-line tool that you run in Terminal, click the Add button (+) under Allowed Commands. In the text field that appears, enter the command and press Return. To remove a command-line tool, select it and click the Remove button (-) under Allowed Commands.

To remove access to a tool, select the tool and click the Remove button (-) under Allowed Tools.

#### Discover Agent Skills and Abilities

Xcode includes built-in expertise that can guide agents to use the best APIs and workflows for high-level tasks. Xcode automatically uses this knowledge based on the prompt that you enter.

For example, when you enter a prompt that includes translating part of your app, Xcode performs localization steps and employs translation subagents. When you enter prompts that include a request to plan, Xcode automatically enters plan mode for exploring ideas without modifying your code.

Alternatively, explicitly invoke a skill using a slash command, such as `/plan` for plan mode. To discover all the skills available in Xcode, type the slash (`/`) character in the message text field and scroll through the list in the pop-up menu. To exit plan mode that’s a workflow skill, type `/exit` and choose `/exit-plan` from the pop-up menu.

#### Customize Agent Environments

Using product-specific configuration files, you can customize agents beyond the options available in Intelligence settings and the coding assistant. For example, you can set a default model, add additional Model Context Protocol (MCP) servers, and create your own skills.

Place the configuration files in agent-specific subfolders in the `~/Library/Developer/Xcode/CodingAssistant` folder that Xcode uses exclusively. For example, place Claude Agent, Codex, and Gemini configuration files in the following folders:

- `~/Library/Developer/Xcode/CodingAssistant/ClaudeAgentConfig`
- `~/Library/Developer/Xcode/CodingAssistant/codex`
- `~/Library/Developer/Xcode/CodingAssistant/gemini`

> **Note**: These configurations only affect agents when you launch them in Xcode.

#### Install Agentic Coding Plug Ins

You can install plug-ins that contain additional subagents, Model Context Protocol (MCP) servers, and skills that agents can use. To manage plug-ins, open Intelligence settings and click the Plug-ins row under Agents in Xcode.

To add a plug-in, click the Add Plug-in button. In the sheet, choose an import option and click Continue. In the next sheet, enter information, such as the URL if you choose Add from URL, and click Continue. In the final sheet, select the components that you want to install and click Install.

## See Also

- [Giving external agents access to Xcode](giving-external-agents-access-to-xcode.md)
  Let agents access your project and Xcode capabilities using the Model Context Protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/extending-and-customizing-agents)*