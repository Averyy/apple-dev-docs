# Setting up coding intelligence

**Framework**: Xcode

Configure coding intelligence to use the model of your choice and other settings.

#### Overview

To use coding intelligence in Xcode, you need to choose a model. You can enable ChatGPT in Xcode or Claude in Xcode, where these models are available, or use another model that you prefer.

First, choose Xcode > Settings and select Intelligence in the sidebar.

![A screenshot of the Intelligence settings showing the About Coding Intelligence and privacy link, the ChatGPT in Xcode and Claude in Xcode models, and the Add a Model Provider button.](https://docs-assets.developer.apple.com/published/33fb806b29f7c5cd9ed60bdf11cb8ea7/coding-assistant-intell-settings%402x.png)

##### Use Chatgpt in Xcode

To use ChatGPT in Xcode (with or without an account):

1. In the ChatGPT in Xcode row, click Turn On.
2. In the dialogs that appear, click Next and then click Turn On ChatGPT.

To sign in to a free ChatGPT account, or a paid account with higher limits:

1. In Intelligence settings, click the ChatGPT in Xcode row.
2. With the ChatGPT in Xcode switch on, click Sign In, and in the next dialog, click Sign In again.
3. In the browser window that appears, follow the instructions to enter your credentials.

To upgrade your free ChatGPT account to a paid account, click Upgrade to ChatGPT Plus on the bottom of the ChatGPT in Xcode settings.

For some models, you can choose a level of reasoning that the model uses while producing a response. Select the level in the Reasoning pop-up menu that appears below the message text field in the coding assistant.

##### Use Claude in Xcode

To use Claude in Xcode:

1. In Intelligence settings, click the Claude in Xcode row.
2. In Claude in Xcode settings, click Sign In.
3. In the browser window that appears, follow the instructions to enter your credentials.

##### Use Another Model Provider

To use another model provider, click the Add a Model Provider button. To add a model that’s hosted on the internet, select Internet Hosted, enter the URL and other details, and click Add in the dialog that appears. To add a model that’s hosted locally on your Mac, select Locally Hosted and enter a port and optional description instead.

![A screenshot of the Intelligence settings showing the Add a Model Provider dialog with the Internet Hosted option selected, and the URL, other controls, and Add button below.](https://docs-assets.developer.apple.com/published/cf190356b892ccb777180a0c01d29cd8/coding-add-model-provider-internet-hosted%402x.png)

If you choose another model, it needs to support the Chat Completions API. In addition, Xcode expects the model to support these endpoints that list models and perform completions:

- `{Model provider URL}/v1/models`
- `{Model provider URL}/v1/chat/completions`

##### Configure Managed Devices

If you want to disable the coding assistant for managed devices, set the `CodingAssistantAllowExternalIntegrations` key to `false` in a mobile device management (MDM) profile. For more information, see [`Device management restrictions for Mac computers`](https://developer.apple.comhttps://support.apple.com/guide/deployment/restrictions-for-mac-depba790e53/web).

## See Also

- [Writing code with intelligence in Xcode](writing-code-with-intelligence-in-xcode.md)
  Generate code, fix bugs fast, and learn as you go with intelligence built directly into Xcode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/setting-up-coding-intelligence)*