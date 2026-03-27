# Setting up coding intelligence

**Framework**: Xcode

Enable third-party coding tools that you want to use in the coding assistant.

#### Overview

To use coding intelligence in Xcode, enable the products in Intelligence settings that you want to use in the coding assistant. When you choose a third-party product and begin entering prompts in the coding assistant, the product can share your project files and other information with their model when processing your requests.

You can enable ChatGPT in Xcode or Claude where these products are available, or use another provider that you prefer. Optionally, enable a provider’s agentic coding tool that has access to Xcode capabilities — such as modifying your project and performing actions — through the Model Context Protocol (MCP). You can then customize agentic coding tools for your specific development needs, such as adding additional MCP servers.

First, choose Xcode > Settings and select Intelligence in the sidebar.  For more information about sharing your project files with third-party products and their models, click “About Intelligence in Xcode & Privacy.”

![A screenshot of the Intelligence settings showing the About Intelligence and Privacy link, the OpenAI and Anthropic providers, and the Add a Provider button.](https://docs-assets.developer.apple.com/published/bb5b02211e540f5d0602eaa21f5262a2/intelligence-settings%402x.png)

To give agentic coding tools that you use outside of Xcode access to your project and Xcode capabilities, see [`Giving external agentic coding tools access to Xcode`](giving-agentic-coding-tools-access-to-xcode.md).

##### Enable Chatgpt in Xcode

To use ChatGPT in Xcode (with or without an account):

1. In Intelligence settings, click OpenAI under Providers and then click ChatGPT in Xcode.
2. In the ChatGPT in Xcode row, click Turn On.
3. In the dialogs that appear, click Next, and then click Turn On ChatGPT.

![A screenshot of the OpenAI settings showing the ChatGPT in Xcode row and the Get button in the Codex row.](https://docs-assets.developer.apple.com/published/202595e7ba54338438efbca3753857fb/intelligence-settings-openai%402x.png)

To sign in to a free ChatGPT account, or a paid account with higher limits:

1. In ChatGPT in Xcode settings, toggle ChatGPT in Xcode on.
2. In the ChatGPT row, click Sign In, and in the next dialog, click Sign In again.
3. In the browser window that appears, follow the instructions to enter your credentials.

To upgrade your free ChatGPT account to a paid account, click Upgrade to ChatGPT Plus at the bottom of the ChatGPT in Xcode settings.

For some models, you can choose a level of reasoning that the model uses while producing a response. In the project editor, select the level in the Reasoning pop-up menu that appears below the message text field in the coding assistant.

To turn off ChatGPT in Xcode, toggle ChatGPT in Xcode off in the OpenAI > ChatGPT in Xcode settings.

##### Enable Codex

When you choose Codex in the coding assistant, it automatically has access to Xcode capabilities using the MCP server that Xcode provides. To use Codex with a ChatGPT account:

1. In the Intelligence > OpenAI settings, click the Get button in the Codex row, and in the dialog that appears, click Install.
2. In the ChatGPT Account row, click the More button (…).
3. Choose Sign In With a ChatGPT Account or Provide an OpenAI API Key from the pop-up menu.
4. In the browser window that appears, follow the instructions to enter your credentials, or in the dialog, enter your key and click Done.

After you download Codex, Xcode automatically updates the download if possible. To manage the Codex download, click the information button next to Codex in Components settings (see [`Downloading and installing additional Xcode components`](downloading-and-installing-additional-xcode-components.md)).

##### Enable Claude Agent

When you choose Claude Agent in the coding assistant, it automatically has access to Xcode capabilities, such as building and testing your app. To use Claude Agent:

1. In Intelligence settings, click Anthropic under Providers.
2. In the Claude Agent row, click Get, and in the dialog that appears, click Install.
3. Optionally, choose a model from the Model pop-up menu.

![A screenshot of the Anthropic settings showing the Claude Agent and Claude rows.](https://docs-assets.developer.apple.com/published/84d810783b809846e9b7c49afb3879e8/intelligence-settings-anthropic%402x.png)

If you have an account, sign in:

1. In the Account row, click the More button (…).
2. Choose Sign In With a Claude.ai Account or Provide an Anthropic API Key from the pop-up menu.
3. In the browser window that appears, follow the instructions to enter your credentials, or in the dialog, enter your key and click Done.

For more information, click “Anthropic Privacy Policy” at the bottom of the Anthropic settings.

After you download Claude Agent, Xcode automatically updates the download if possible. To manage the Claude Agent download, click the information button next to Claude Agent in Components settings (see [`Downloading and installing additional Xcode components`](downloading-and-installing-additional-xcode-components.md)).

##### Enable Claude

To use Claude:

1. In Intelligence > Anthropic settings, click the Claude row.
2. In Claude settings, click Sign In in the Claude row.
3. In the browser window that appears, follow the instructions to enter your credentials.

For more information about Anthropic products, click “Anthropic Terms of Use” at the bottom of the Anthropic settings.

##### Customize the Codex and Claude Agent Environments

You can customize the Codex and Claude Agent agentic coding tools, beyond the options that you see in Intelligence settings and the coding assistant, using product-specific configuration files. For example, you can set a default model, add additional MCP servers, and create skills. Place the configuration files in the respective Codex and Claude Agent folders that Xcode uses exclusively:

- `~/Library/Developer/Xcode/CodingAssistant/codex`
- `~/Library/Developer/Xcode/CodingAssistant/ClaudeAgentConfig`

> **Note**: Configure agentic coding tools that you run external to Xcode separately in the locations those products recommend.

##### Use Another Provider

To use another provider, click the Add a Provider button under Providers in Intelligence settings. To add a provider that’s hosted on the internet, select Internet Hosted, enter the URL and other details, and click Add in the dialog that appears. To add a provider that’s hosted locally on your Mac, select Locally Hosted and enter a port and optional description instead.

![A screenshot of the Add a Provider dialog with the Internet Hosted option selected, and the URL, other controls, and Add button below.](https://docs-assets.developer.apple.com/published/6ffb3d5842177cdec54667de5e2ebac6/intelligence-settings-add-provider%402x.png)

If you add another provider, it needs to support the Chat Completions API. In addition, Xcode expects the provider to support these endpoints that list models and perform completions:

- `{Model provider URL}/v1/models`
- `{Model provider URL}/v1/chat/completions`

##### Configure Managed Devices

If you want to turn off the coding assistant for managed devices, set the `CodingAssistantAllowExternalIntegrations` key to `false` in a mobile device management (MDM) profile. For more information, see [`Device management restrictions for Mac computers`](https://developer.apple.comhttps://support.apple.com/guide/deployment/restrictions-for-mac-depba790e53/web).

## See Also

- [Writing code with intelligence in Xcode](writing-code-with-intelligence-in-xcode.md)
  Generate code, fix bugs fast, and learn as you go with intelligence built directly into Xcode.
- [Giving external agentic coding tools access to Xcode](giving-agentic-coding-tools-access-to-xcode.md)
  Let agentic coding tools access your project and Xcode capabilities using the Model Context Protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/setting-up-coding-intelligence)*