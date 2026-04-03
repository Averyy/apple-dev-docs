# Setting up coding intelligence

**Framework**: Xcode

Enable third-party coding tools that you want to use in the coding assistant.

#### Overview

To use coding intelligence in Xcode, go to the Intelligence settings and turn on the agent and chat products that you want to use. Choose Xcode > Settings and select Intelligence in the sidebar. Where available, you can turn on Claude or ChatGPT in Xcode. You can also use coding tools from other providers.

![A screenshot of the Intelligence settings showing the About Intelligence and Privacy link, and the Agents, Model Context Protocol, and Chat setting sections.](https://docs-assets.developer.apple.com/published/c929c7d8597d928bc77b7ebe389c7910/intelligence-settings%402x.png)

After you enable coding tools in the Intelligence settings and begin entering prompts in the coding assistant, that product can share your project files and other information with its model when processing your requests. For more information about sharing your project files with third-party products and their models, click “About Intelligence in Xcode & Privacy…” in the Intelligence settings.

When you use agents, you have control over the Xcode capabilities that they have when modifying your project and performing actions through the Model Context Protocol (MCP). You can also customize agents for your specific development needs.

To give agents that you use outside of Xcode access to your project and Xcode capabilities, see [`Giving external agents access to Xcode`](giving-external-agents-access-to-xcode.md).

##### Enable Claude Agent

When you choose Claude Agent in the coding assistant, it automatically has access to Xcode capabilities, such as building and testing your app. To use Claude Agent:

1. In Intelligence settings, click Get in the Claude Agent row under Agents.
2. In the dialog that appears, click Install.

If you have an account, sign in:

1. In Claude Agent settings, click the More button (…) in the Account row.
2. Choose Sign In With a Claude.ai Account or Provide an Anthropic API Key from the pop-up menu.
3. In the browser window that appears, follow the instructions to enter your credentials, or in the dialog, enter your API key and click Done.

![A screenshot of the Claude Agent settings showing the Account row.](https://docs-assets.developer.apple.com/published/c8e61a06d618e62ed434180f94df3b2e/intelligence-settings-claude-agent%402x.png)

For more information, click “Anthropic’s Privacy Policy” at the bottom of the Claude Agent settings.

After you download Claude Agent, Xcode automatically updates the download if possible. To manage the Claude Agent download, click the information button next to Claude Agent in Components settings (see [`Downloading and installing additional Xcode components`](downloading-and-installing-additional-xcode-components.md)).

##### Enable Codex

When you choose Codex in the coding assistant, it automatically has access to Xcode capabilities. To use Codex with a ChatGPT account:

1. In Intelligence settings, click Get in the Codex row under Agents.
2. In the dialog that appears, click Install.
3. In Codex settings, click the More button (…) in the ChatGPT Account row.
4. Choose Sign In With a ChatGPT Account or Provide an OpenAI API Key from the pop-up menu.
5. In the browser window that appears, follow the instructions to enter your credentials, or in the dialog, enter your API key and click Done.

![A screenshot of the Codex settings showing the ChatGPT Account row.](https://docs-assets.developer.apple.com/published/44bd09e63ac39c402805c375f048ca47/intelligence-settings-codex%402x.png)

For more information, click “OpenAI Terms of Use…” at the bottom of the Codex settings.

After you download Codex, Xcode automatically updates the download if possible. To manage the Codex download, click the information button next to Codex in Components settings (see [`Downloading and installing additional Xcode components`](downloading-and-installing-additional-xcode-components.md)).

##### Customize the Claude Agent and Codex Environments

You can customize Claude Agent and Codex, beyond the options that you see in Intelligence settings and the coding assistant, using product-specific configuration files. For example, you can set a default model, add additional MCP servers, and create skills. Place the configuration files in the respective Claude Agent and Codex folders that Xcode uses exclusively:

- `~/Library/Developer/Xcode/CodingAssistant/ClaudeAgentConfig`
- `~/Library/Developer/Xcode/CodingAssistant/codex`

> **Note**: Configurations you make here only affect agents when you launch them in Xcode.

##### Restrict Agent Access to Command Line and Xcode Tools

If you want finer control over the tasks agents can perform on your behalf, you can limit access of all agents that you use in Xcode to specific MCP and command-line tools. To manage these permissions, click the Permissions row under Agents in Xcode.

To give access to a command-line tool that you run in Terminal, click the Add button (+) under Allowed Commands. In the text field that appears, enter the command and press Return. To remove a command-line tool, select it and click the Remove button (-) under Allowed Commands.

To remove access to an MCP tool that you previously granted permission to use in coding assistant, select the tool and click the Remove button (-) under Allowed Tools.

##### Enable Chatgpt in Xcode

To use ChatGPT in Xcode (with or without an account):

1. In Intelligence settings, click Turn On in the ChatGPT in Xcode row under Chat.
2. In the dialogs that appear, click Next, and then click Turn On ChatGPT.

![A screenshot of the OpenAI settings showing the ChatGPT in Xcode row and the Get button in the Codex row.](https://docs-assets.developer.apple.com/published/abb93a83403e10e9ad911c2b9ffbb91c/intelligence-settings-chatgpt-in-xcode%402x.png)

To sign in to a free ChatGPT account, or a paid account with higher limits:

1. In ChatGPT in Xcode settings, toggle ChatGPT in Xcode on.
2. In the ChatGPT row, click Sign In, and in the next dialog, click Sign In again.
3. In the browser window that appears, follow the instructions to enter your credentials.

To upgrade your free ChatGPT account to a paid account, click Upgrade to ChatGPT Plus at the bottom of the ChatGPT in Xcode settings.

For some models, you can choose the level of reasoning that the model uses while producing a response. In the project editor, select the level in the Reasoning pop-up menu that appears below the message text field in the coding assistant.

For more information about OpenAI products, click “OpenAI Terms of Use…” at the bottom of the ChatGPT in Xcode settings.

To turn off ChatGPT in Xcode, toggle ChatGPT in Xcode off in the ChatGPT in Xcode settings.

##### Enable Claude Sonnet Opus

To use Claude Sonnet & Opus:

1. In Intelligence settings, click Claude Sonnet & Opus under Chat.
2. In the Claude row, click Sign In.
3. In the browser window that appears, follow the instructions to enter your credentials.

![A screenshot of the Claude settings showing the Sign In button and information links.](https://docs-assets.developer.apple.com/published/965db5fc1727b6c9d6c04e035a2c52b4/intelligence-settings-claude%402x.png)

For more information about Anthropic products, click “Anthropic Terms of Use…” at the bottom of the Claude settings.

##### Use Another Chat Provider

To use another chat provider, click the Add a Chat Provider button under Chat. To add a provider that’s hosted on the internet, select Internet Hosted, enter the URL and other details, and click Add in the dialog that appears. To add a provider that’s hosted locally on your Mac, select Locally Hosted and enter a port and optional description instead.

![A screenshot of the Add a Provider dialog with the Internet Hosted option selected, and the URL, other controls, and Add button below.](https://docs-assets.developer.apple.com/published/6ffb3d5842177cdec54667de5e2ebac6/intelligence-settings-add-provider%402x.png)

If you add another provider, it needs to support the Chat Completions API. In addition, Xcode expects the provider to support these endpoints that list models and perform completions:

- `{Model provider URL}/v1/models`
- `{Model provider URL}/v1/chat/completions`

##### Configure Managed Devices

If you want to turn off the coding assistant for managed devices, set the `CodingAssistantAllowExternalIntegrations` key to `false` in a mobile device management (MDM) profile. For more information, see [`Device management restrictions for Mac computers`](https://developer.apple.comhttps://support.apple.com/guide/deployment/restrictions-for-mac-depba790e53/web).

## See Also

- [Writing code with intelligence in Xcode](writing-code-with-intelligence-in-xcode.md)
  Generate code, fix bugs fast, and learn as you go with intelligence built directly into Xcode.
- [Giving external agents access to Xcode](giving-external-agents-access-to-xcode.md)
  Let agents access your project and Xcode capabilities using the Model Context Protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/setting-up-coding-intelligence)*