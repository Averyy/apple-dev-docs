# Writing code with intelligence in Xcode

**Framework**: Xcode

Generate code, fix bugs fast, and learn as you go with intelligence built directly into Xcode.

#### Overview

The coding intelligence features in Xcode help you write code, navigate unfamiliar codebases, find opportunities for new features, fix or refactor existing code, and generate documentation along the way.

![A screenshot of the project editor with the coding assistant in the sidebar on the left and a source file open in the source editor on the right. The coding assistant shows a prompt that asks about the code and a response from the model.](https://docs-assets.developer.apple.com/published/46900d94902d87e36a648cfdbd93abb8/coding-assistant-hero%402x.png)

You interact with a large language model of your choice using natural language prompts to ask questions and give instructions. The model refines the responses to your prompts based on your previous interactions and project context. You stay in control over changes to your project by applying suggestions automatically or reviewing and applying them selectively yourself. Xcode maintains a history of your conversations with the model so that you can review past responses, track changes, and return to any previous state of your project.

##### Set Up Coding Intelligence

Before you start, you need a model. With just a few clicks, you can enable ChatGPT or add any model provider you prefer:

1. In Xcode, choose Xcode > Settings.
2. Select Intelligence in the sidebar.
3. Turn on ChatGPT (where available) as your model, or click the button to add another model provider that’s either hosted on the internet or locally on your Mac.

![A screenshot of the Intelligence settings showing the About Coding Intelligence and privacy link, the ChatGPT Turn On button, and the Add a Model provider button.](https://docs-assets.developer.apple.com/published/138be234fc7cf591ded7d5376289227f/coding-assistant-intell-settings%402x.png)

##### Display the Coding Assistant

In the upper-left corner of the toolbar, click the button to the right of the navigator button to open the coding assistant area in the sidebar or press Command-0. Here, you can enter prompts, see responses, start and navigate between conversations, rollback changes, and more.

![A screenshot that shows the coding assistant sidebar cropped with a sample prompt and response displayed. The screenshot is annotated with callouts for the buttons, menus, and areas of the coding assistant.](https://docs-assets.developer.apple.com/published/4e3978f7682165585db1c31df848d35c/coding-assistant-anatomy%402x.png)

If a Set Up Intelligence button appears in the sidebar instead, choose a coding intelligence model, such as ChatGPT, in Xcode > Settings > Intelligence.

##### Explore Unfamiliar Code

At any time, you can ask Xcode to explain code and find files to implement a new feature or just to familiarize yourself with some code. For example, if you download the [`Landmarks: Building an app with Liquid Glass`](https://developer.apple.com/documentation/SwiftUI/Landmarks-Building-an-app-with-Liquid-Glass) sample app, you can select code and ask questions.

![A screenshot of the coding assistant in the sidebar and a source file open in the source editor on the right. The coding assistant shows the results of entering the prompt, What does this app do? in the conversation area.](https://docs-assets.developer.apple.com/published/197a77b34dbad59ca60fbbefdd40c66c/coding-assistant-explore-code-question%402x.png)

Xcode responds under your prompt in the conversation area of the coding assistant. The response may contain content that you can interact with. For example, if the response references a filename, click the arrow button next to the filename to open it in the source editor. To continue the conversation with the coding assistant, enter follow-up prompts, like:

When you enter another prompt, the coding assistant appends your prompt and response to the conversation. Xcode maintains an entire transcript of your interactions with the model so you can refer back to them.

##### Learn About Symbols and Code

In the source editor, Control-click a symbol or code selection and choose Show Coding Tools from the contextual menu, or press Command-Option-0. Then click Explain, or enter a more specific prompt in the coding tools popover. The coding assistant displays the prompt and its response in the conversation area.

![A screenshot that shows the project navigator in the sidebar and the source editor on the right with a code snippet selected and the Show Coding Tools popover displayed with the Explain button.](https://docs-assets.developer.apple.com/published/63ef5711ba15d3c99e38f4ca3b51d306/coding-assistant-show-coding-tools%402x.png)

Alternatively, click the coding assistant button in the source editor gutter to display the coding tools popover.

##### Generate or Modify Code

Give Xcode specific instructions on how to generate or modify code. If you aren’t getting the result you expected, try breaking down your question or adding more detailed instruction. Between each prompt, review and validate the code changes with a preview or playground, and continue iterating on your app by adjusting your prompts to get the behavior you’re looking for.

For example, if you’re new to Swift and SwiftUI, you can code along with the modifications that Xcode makes. Start with a Swift app that you create from a template and instruct Xcode to make incremental changes, such as:

While working on a response, Xcode displays progress messages in the message text field before posting its response in the conversation area. The response may contain a description of the changes, including some steps or code changes.

![A screenshot of the coding assistant in the sidebar on the left and a file opened in the source editor on the right. The coding assistant shows the prompt, some steps, and a code snippet, along with next steps.](https://docs-assets.developer.apple.com/published/af29124bdd4c6efddd41251f5a96f6a0/coding-assistant-write-code%402x.png)

The changes may go beyond what you asked for or build on your previous prompts. The response may contain next steps and ask you a follow-up question. Xcode puts you in control, where you lead and redirect the conversation as needed to steer the model in the direction you’d like to go.

You can either answer the question (continue the conversation with the assistant) or enter a new prompt.

To generate code about specific symbols while in the source editor, you can use the coding tools popover. Control-click a symbol and choose Show Coding Tools from the contextual menu, then enter a prompt in the coding tools popover.

##### Apply Changes to Your Code

You can see code changes that Xcode automatically applies to your files as file  in the conversation. These snippets show the modified or added file, and clicking on them takes you to that specific change in the source editor.

> 💡 **Tip**: Use snippets to navigate through all of the changes that Xcode applies and review them in the source editor.

If you want Xcode to automatically edit your code, turn on Automatically Apply Changes by clicking button at the lower-right corner of the sidebar. The response may contain content that you can interact with. For example, click a code listing to open changes in the source editor. Xcode uses multicolor change bars to highlight the lines of code that it changes using coding intelligence.

To undo changes, click Revert above the message text field. To reapply the changes, click Reapply. Alternatively, click the History button in the upper-right corner of the sidebar, to see a history of changes and roll them back by prompt (see [`Rollback changes using the conversation history`](writing-code-with-intelligence-in-xcode#Rollback-changes-using-the-conversation-history.md)).

If you turn the automatically apply button off, Xcode proposes changes to your code instead of applying them and labels them as “Proposed Changes” in the conversation. The response may describe the code changes that the assistant suggests and contain proposed code that you can selectively apply or paste into your files. To apply a proposed change, click the code in the response and click Apply. To apply all the suggested changes, click the Apply button above the message text field.

![A screenshot that shows the coding assistant on the left containing a proposed changes response with the source code opened on the right highlighting the proposed changes with a multicolor change bar in the gutter.](https://docs-assets.developer.apple.com/published/3fc97363f685799968bbbf0bf55dc2b9/coding-assistant-propose-code%402x.png)

##### Customize the Context of Your Prompts

By default, Xcode automatically gathers relevant context to send to the model, based on your prompt and the conversation history. In addition to the automatic context, you can reference specific symbols and files, upload attachments, or refer to a selection in the source editor by mentioning it in your prompt.

You can add specific references to symbols and files by typing the `@` character and choosing a symbol or file:

![A screenshot that highlights the coding assistant at the bottom of the sidebar. There’s an at-character in the message text field, and a completion menu shows suggested symbols and filenames the person can use.](https://docs-assets.developer.apple.com/published/4689647737d52ad34a18a3207844aa01/coding-assistant-enter-symbols%402x.png)

To add additional files from outside your project, choose “Upload files” from the Attachments pop-up menu in the lower-left corner, under the message text field, and select the files to upload from the dialog.

The Project Context button in the lower-right corner of the sidebar is on by default. This allows Xcode to share relevant code and other context from your project with the model. To see the files and search terms that Xcode used, click the information icon next to Project Context if it appears in the response. To narrow the scope of the project files, turn off the automatically search feature and add explicit references to files and symbols in your prompt.

![A screenshot of the coding assistant in the sidebar on the left and the source editor on the right with the Project Context information popover overlaying both panes.](https://docs-assets.developer.apple.com/published/6c1a80436172fb762ef2f5ca2f78fb85/coding-assistant-project-context%402x.png)

##### Generate Playgrounds and Previews

Playgrounds and previews are a great way to experiment with new code without modifying your app. Use playgrounds to run and display code snippets in the canvas, and use previews to validate UI code across platforms. Xcode generates playground and preview code that may contain sample data to help you better understand and visualize the code in the canvas.

To add a playground macro to your project, open coding tools and choose Generate a Preview:

![A screenshot that shows the Show Coding Tools popover open and the Generate a Playground button highlighted.](https://docs-assets.developer.apple.com/published/6df2038aa6b07591a47390d652b053df/coding-assistant-generate-playground%402x.png)

Xcode shows the results of the playground, and for SwiftUI files, the previews, in the canvas area. If the canvas isn’t open, choose Editor > Canvas to show it, then click Resume.

![A screenshot that shows the project navigator in the sidebar, a file opened in the source editor with the playground code generated, and the playground run in the canvas on the right.](https://docs-assets.developer.apple.com/published/11757040038cf6aa32a03d9f915f4f39/coding-assistant-run-playground%402x.png)

To learn more about the playground macro, see [`Running code snippets using the playground macro`](running-code-snippets-using-the-playground-macro.md). For previews, see [`Previewing your app’s interface in Xcode`](previewing-your-apps-interface-in-xcode.md).

##### Fix Your Code

If you encounter a compilation warning or error while building your app, Xcode may be able to generate a fix for you.

The source editor highlights any issues with a red underline and presents an issue summary and icon. Click the icon to show more information about the issue, then click Generate next to “Generate Fix for Issue”. Xcode applies the model-generated change and shows the fix in the coding assistant.

![A screenshot that shows a file open in the source editor with a Fix-it dialog with the syntax error message and a Generate Fix for Issue button.](https://docs-assets.developer.apple.com/published/b80445202bd1bb6df65c403107fbb778/coding-assistant-generate-fix-it%402x.png)

##### Generate Documentation

Let Xcode draft your API documentation for you. Select a symbol in the source editor and click the coding intelligence icon that appears. In the dialog, click Document.

![A screenshot of the project navigator on the left, a file open in the source editor with generated DocC style comments above the class name.](https://docs-assets.developer.apple.com/published/36d2e3669dcf287ea3ef7ad00b0e5df6/coding-assistant-generate-docs%402x.png)

Xcode can add [`DocC`](https://developer.apple.com/documentation/DocC)-style comments to the source file above the symbol. For example, select a class and Xcode adds documentation for the class, its properties and methods, including the method parameters.

Xcode displays coding intelligence controls at the bottom of the source editor that summarizes the change. To see the response in the conversation area of the coding assistant, click the coding assistant button. To undo changes, click the Revert button.

![A screenshot of the coding assistant dialog that appears in the source editor.](https://docs-assets.developer.apple.com/published/1293ebce1687437618b8b81232b2b88b/coding-assistant-source-editor-dialog%402x.png)

##### Browse Previous Conversations

At any time you can review the conversations you have with the coding assistant. A conversation is a thread of prompts and responses that appears in the conversation area. For example, you can ask the model to make a series of changes for a feature you’re working on in the same conversation. Then create a new conversation for another feature that’s in a different part of your code.

You can manage your conversations in the conversation area or using the Conversation pop-up menu in the toolbar to:

- Review prompts and responses in the same conversation by scrolling up or down in the list of prompts.
- Show or hide a response by clicking the disclosure triangle to the right of the prompt.
- Jump to a recent or previous conversation by choosing the conversation from the menu.
- Remove previous conversations by choosing Clear All from the menu.
- Start a new conversation by clicking the New Conversation button on the left in the toolbar, then enter a prompt in the message text field below.

![A screenshot that shows the coding assistant area with the conversation pop-up menu open and containing multiple conversations to choose from.](https://docs-assets.developer.apple.com/published/4d3b25d7b3f4cfc3ab1b886ed9317190/coding-assistant-conversation-menu%402x.png)

##### Rollback Changes Using the Conversation History

Use the conversation history that Xcode maintains to rollback changes to a known state of your project, or to review changes across multiple files in your project.

To rollback changes in a conversation by prompt, choose the conversation from the Conversation pop-up menu and click the History button. Xcode shows a chronological list of your prompts with a slider on the right. Move the slider from the bottom to the top to unwind changes in the order that you made them. Move the slider up to remove changes, that Xcode shows on the right, and move the slider down to restore changes in the next prompt.

![A screenshot that shows the History view in the sidebar with the slider on the right, and the Cancel and Restore buttons below. The changes for the current state are in the source editor to the right.](https://docs-assets.developer.apple.com/published/2f4946535e32d9027b19b8b36007f4fc/coding-assistant-history-view%402x.png)

Xcode retains all the edits it made after that state in case you decide to roll forward any changes later. After scrubbing back to the point you would like to restore to, click the Restore button to update your project files to the state from this point on. To keep all the changes in a conversation regardless of the current slider position, click Cancel.

> **Note**: To use the History feature, your project must have a Git repository. To create a local repository, choose Integrate > New Git Repository. Xcode doesn’t make changes to your repository, but its history relies on your project’s Git history for reference purposes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/writing-code-with-intelligence-in-xcode)*