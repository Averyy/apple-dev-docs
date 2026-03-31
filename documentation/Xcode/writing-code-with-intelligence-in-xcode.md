# Writing code with intelligence in Xcode

**Framework**: Xcode

Generate code, fix bugs fast, and learn as you go with intelligence built directly into Xcode.

#### Overview

The coding intelligence features in Xcode help you write code, navigate unfamiliar codebases, find opportunities for new features, fix or refactor existing code, and generate documentation along the way.

![A screenshot of the project editor with the coding assistant in the sidebar on the left and a source file open in the source editor on the right. The coding assistant shows a prompt that asks to change the code and a response from the model.](https://docs-assets.developer.apple.com/published/d139d2ad34923a14c5a7eb7dfac855a1/coding-assistant-hero%402x.png)

You interact with a large language model using natural language prompts to ask questions and give instructions. The model refines the responses to your prompts based on your previous interactions and project context. You choose whether to use a third-party agent or chat product to help write code.

If you use an agent, Xcode can refine and iterate on a goal with less guidance and perform actions, such as fixing build errors after writing code. You decide what external tools, command-line or otherwise, an agent may use in responses to your prompts.

If you use a chat product, you stay in control over changes to your project by applying suggestions automatically or reviewing and applying them selectively yourself. Xcode maintains a history of your conversations with the model so that you can review past responses, track changes, and return to any previous state of your project.

##### Display the Coding Assistant and Choose a Third Party Agent or Chat Provider

To open the coding assistant area in the sidebar, click the button to the right of the navigator button in the upper-left corner of the toolbar, or press Command-0. Here, you can enter prompts, see responses, start and navigate between conversations, undo changes, and more.

![A screenshot that shows the coding assistant sidebar cropped with a sample prompt and response displayed. The screenshot is annotated with callouts for the buttons, menus, and areas of the coding assistant.](https://docs-assets.developer.apple.com/published/1a0c9501a148b6d4a1cc598eea0428e0/coding-assistant-anatomy%402x.png)

If a Set Up button appears in the coding assistant, click the button and enable a coding intelligence agent or chat provider in Xcode > Settings > Intelligence, as described in [`Setting up coding intelligence`](setting-up-coding-intelligence.md).

In the coding assistant, click the Start New Conversation button on the left of the toolbar. In the pop-up menu, choose an agent under Agents or a model under Chat. The agent or chat model that you choose appears in the message text field below.

If you choose an agent, it automatically has access to some Xcode capabilities, such as building your app, searching Apple documentation, and more. When you enter a prompt, Xcode may display a dialog asking for permission to access files or use a tool before responding. For more information about settings for agents, see [`Restrict agent access to command-line and Xcode tools`](setting-up-coding-intelligence#Restrict-agent-access-to-command-line-and-Xcode-tools.md).

##### Explore Unfamiliar Code

At any time, you can ask Xcode to explain code and find files to implement a new feature or just to familiarize yourself with some code. For example, if you download the [`Landmarks: Building an app with Liquid Glass`](https://developer.apple.com/documentation/SwiftUI/Landmarks-Building-an-app-with-Liquid-Glass) sample app, you can select code and ask questions, such as:

- *What does this app do?*

![A screenshot of the coding assistant in the sidebar and a source file open in the source editor on the right. The coding assistant shows the results of entering the prompt, What does this app do? in the conversation area.](https://docs-assets.developer.apple.com/published/e6fc64d80db8b1daaac98939347e7f1e/coding-assistant-explore-code-question%402x.png)

Xcode responds under your prompt in the conversation area of the coding assistant. The response may contain content that you can interact with. For example, if the response references a filename, click the arrow button next to the filename to open it in the source editor. To continue the conversation with the coding assistant, enter follow-up prompts, like:

- *Tell me more about the views that display this object*

When you enter another prompt, the coding assistant appends your prompt and response to the conversation. Xcode maintains an entire transcript of your interactions with the agent or model so you can refer back to them.

##### Learn About Symbols and Code

In the source editor, Control-click a symbol or code selection and press Command-Option-0 or choose Show Coding Tools > Show Coding Tools from the contextual menu. Then click Explain, or enter a more specific prompt in the coding tools popover. The coding assistant displays the prompt and its response in the conversation area.

![A screenshot that shows the Project navigator in the sidebar and the source editor on the right with a code snippet selected and the Show Coding Tools popover displayed with the Explain button.](https://docs-assets.developer.apple.com/published/b5c3130df3836a8afa02a794cf55d7a8/coding-assistant-show-coding-tools%402x.png)

Alternatively, click the coding assistant button in the source editor gutter to display the coding tools popover.

##### Enter a Sequence of Prompts to Reach Your Goal

Give Xcode specific instructions on how to generate or modify your code. If you aren’t getting results that you expect, try breaking down your question or adding more detailed instructions.

For example, if you’re new to Swift and SwiftUI, you can code along with the modifications that Xcode makes. Start with a Swift app that you create from a template and instruct Xcode to make incremental changes, such as:

- *Add properties and methods to a class*
- *Create a list view and wrap it in a NavigationStack*
- *Add the ability to edit the properties of items in the list view*
- *Change the list view to a table view showing all the properties*

Between each prompt, review and validate the code changes, and continue iterating on your app by adjusting your prompts to get the results you want.

The response may contain next steps and ask you follow-up questions. You can either answer the questions (continue the conversation with the assistant) or enter a new prompt.

##### Generate or Modify Code

Enter your prompts in the message text field at the bottom of the coding assistant or press Command-Option-0 in the source editor and enter a prompt in the coding tools popover.

While working on a response, Xcode displays progress messages in the text field before posting its response in the conversation area. The response may contain a description of the changes, including some steps or code changes.

![A screenshot of the coding assistant in the sidebar on the left and a file opened in the source editor on the right. The coding assistant shows the prompt, a code snippet, and a description of the changes.](https://docs-assets.developer.apple.com/published/e2a56c12ba3a526b5d5e2c30e37de5dc/coding-assistant-write-code%402x.png)

If you choose an agent, Xcode may iterate on a response, build your app to verify the code, and fix build warnings and errors automatically.

The response may contain content that you can interact with. For example, click a code change to open it in the source editor. Xcode uses multicolor change bars to highlight changes made using intelligence.

To undo changes, click the Undo Changes button to the right of the message text field.

##### Apply Changes to Your Code

If you use a chat product, you have finer control over when Xcode modifies your code.

The “Automatically apply code changes” button in the lower-right corner of the sidebar is on by default. If you turn the “Automatically apply code changes” button off, Xcode proposes changes to your code instead of applying them and labels them as “Proposal” in the conversation area.

The response may describe the code changes that the assistant suggests and contain proposed code that you can selectively apply or paste into your files.

To apply a proposed change, click the code snippet in the response and click Apply in the dialog that appears. If the change adds a new file, click Create New File in the dialog.

![A screenshot that shows the coding assistant on the left containing a proposed changes response with the source code opened on the right highlighting the proposed changes with a multicolor change bar in the gutter.](https://docs-assets.developer.apple.com/published/842c64a904313babbb12ec71a131b8ab/coding-assistant-propose-code%402x.png)

##### Customize the Context of Your Prompts

By default, Xcode automatically gathers relevant context to send to the model, based on your prompt and the conversation history. In addition to the automatic context, you can reference specific symbols and files, upload attachments, or refer to a selection in the source editor by mentioning it in your prompt.

You can add specific references to symbols and files by typing the `@` character and choosing a symbol or file:

![A screenshot that highlights the coding assistant at the bottom of the sidebar. There’s an at-character in the message text field, and a completion menu shows suggested symbols and filenames the person can use.](https://docs-assets.developer.apple.com/published/4095518d647b895691447f30a15d31e6/coding-assistant-enter-symbols%402x.png)

To add additional files from outside your project, choose “Upload files” from the Attachments pop-up menu in the lower-left corner, under the message text field, and select the files to upload from the dialog.

If you use a chat product, a Project Context button appears in the lower-right corner of the sidebar and is on by default. This allows Xcode to share relevant code and other context from your project with the model. To narrow the scope of the project files, you can turn off the automatic search feature and add explicit references to files and symbols in your prompt instead.

##### Generate Playgrounds and Previews

Playgrounds and previews are a great way to experiment with new code without modifying your app. Use playgrounds to run and display code snippets in the canvas, and use previews to validate UI code across platforms. Xcode generates playground and preview code that may contain sample data to help you better understand and visualize the code in the canvas.

To add a playground macro to your project, open coding tools and choose Generate a Playground:

![A screenshot that shows the coding tools popover open and the Generate a Playground button highlighted.](https://docs-assets.developer.apple.com/published/6df2038aa6b07591a47390d652b053df/coding-assistant-generate-playground%402x.png)

Xcode shows the results of the playground, and for SwiftUI files, the previews, in the canvas area. If the canvas isn’t open, choose Editor > Canvas to show it, then click Resume.

![A screenshot that shows the Project navigator in the sidebar, a file opened in the source editor with the playground code generated, and the playground run in the canvas on the right.](https://docs-assets.developer.apple.com/published/3a6c8a3b84e1a307453225bd587cd3aa/coding-assistant-run-playground%402x.png)

To learn more about the playground macro, see [`Running code snippets using the playground macro`](running-code-snippets-using-the-playground-macro.md). For previews, see [`Previewing your app’s interface in Xcode`](previewing-your-apps-interface-in-xcode.md).

##### Fix Your Code

If you encounter a compilation warning or error while building your app, Xcode may be able to generate a fix for you.

The source editor highlights any issues with a red underline and presents an issue summary and icon. Click the icon to show more information about the issue, then click Generate next to “Generate Fix for Issue”. Xcode applies the model-generated change and shows the fix in the coding assistant.

![A screenshot that shows the issue navigator on the left with an issue selected and a file open in the source editor with a Fix-it dialog with the syntax error message and a Generate button.](https://docs-assets.developer.apple.com/published/0702ce2d359f75c21bfd3249242209bc/coding-assistant-generate-fix-it%402x.png)

If you choose an agent, Xcode may fix errors and warnings in generated code for you.

##### Generate Documentation

Let Xcode draft your API documentation for you. In the source editor, select a symbol that needs documentation comments and click the coding intelligence icon that appears in the gutter. In the coding tools dialog, click Document.

![A screenshot of the Project navigator on the left, a file open in the source editor with generated DocC style comments above the structure name.](https://docs-assets.developer.apple.com/published/7316da7c55972c15a5a1f9957cf4a3fe/coding-assistant-generate-docs%402x.png)

Xcode can add [`DocC`](https://developer.apple.comhttps://www.swift.org/documentation/docc/)-style comments to the source file above the symbol. For example, select a class and Xcode adds documentation for the class, its properties and methods, including the method parameters.

Xcode displays coding intelligence controls at the bottom of the source editor that summarizes the change. To see the response in the conversation area of the coding assistant, click the coding assistant button. To undo changes, click the Revert button.

![A screenshot of the coding assistant dialog that appears in the source editor.](https://docs-assets.developer.apple.com/published/1293ebce1687437618b8b81232b2b88b/coding-assistant-source-editor-dialog%402x.png)

To view your documentation in Xcode, choose Product > Build Documentation.

##### Browse Previous Conversations

At any time you can review the conversations you have with the coding assistant. A conversation is a thread of prompts and responses that appears in the conversation area. For example, you can ask the model to make a series of changes for a feature you’re working on in the same conversation. Then create a new conversation for another feature that’s in a different part of your code.

You can manage your conversations in the conversation area or using the conversation pop-up menu in the middle of the toolbar to:

- Review prompts and responses in the same conversation by scrolling up or down in the list of prompts.
- Jump to a recent or previous conversation by choosing the conversation from the menu.
- Remove previous conversations by choosing Clear Recents from the menu.
- Start a new conversation by clicking the Start New Conversation button on the left of the toolbar and choosing an agent or chat product from the pop-up menu.

![A screenshot that shows the coding assistant area with the conversation pop-up menu open and containing multiple conversations and previous conversations to choose from.](https://docs-assets.developer.apple.com/published/7f2db36cb30793a764e8807702a53f8b/coding-assistant-conversation-menu%402x.png)

##### Rollback Changes Using the Conversation History

Use the conversation history that Xcode maintains to rollback changes to a known state of your project, or to review changes across multiple files in your project.

To rollback changes in a conversation by prompt, choose the conversation from the Conversation pop-up menu and click the History button. Xcode shows a chronological list of your prompts with a slider on the right. Move the slider from the bottom to the top to unwind changes in the order that you made them. Move the slider up to remove changes, that Xcode shows on the right, and move the slider down to restore changes in the next prompt.

![A screenshot that shows the History view in the sidebar with the slider on the right, and the Cancel and Restore buttons below. The changes for the current state are in the source editor to the right.](https://docs-assets.developer.apple.com/published/2bb7fc6808d71eb1e28f8a76ca1a571e/coding-assistant-history-view%402x.png)

Xcode retains all the edits it made after that state in case you decide to roll forward any changes later. After scrubbing back to the point you would like to restore to, click the Restore button to update your project files to the state from this point on. To keep all the changes in a conversation regardless of the current slider position, click Cancel.

> **Note**: To use the History feature, your project must have a Git repository. If you don’t have a repository, click the Create Repository button that appears when you click the History button. Alternatively, choose Integrate > New Git Repository to create a local repository. Xcode doesn’t make changes to your repository, but its history relies on your project’s Git history for reference purposes.

## See Also

- [Setting up coding intelligence](setting-up-coding-intelligence.md)
  Enable third-party coding tools that you want to use in the coding assistant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/writing-code-with-intelligence-in-xcode)*