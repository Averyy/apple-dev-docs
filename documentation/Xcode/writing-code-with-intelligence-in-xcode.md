# Writing code with intelligence in Xcode

**Framework**: Xcode  
**Role**: Article

Start conversations with an agent in Xcode to generate code, navigate unfamiliar codebases, and fix or refactor existing code.

## Overview

Open the coding assistant, enter your prompts, and see the results in the transcript and artifacts panes. Undo changes or roll them back using the conversation history. Then organize your conversations with an agent by feature or approach using the conversation sidebar.

To set up agents in Intelligence settings before you begin, see [Setting up coding intelligence](./setting-up-coding-intelligence.md).

## Start conversations with an agent

After you enable one or more agents, you can start conversations in different places in your project where it’s most convenient for you.

To start a conversation with a specific agent, click the Coding Assistant button above the navigation area or press Command-0. Then click the New Conversation button above the conversation sidebar, if you only have one agent set up. Otherwise, choose an agent from the pop-up menu that appears.

![A screenshot that shows the Coding Assistant button selected with the conversation list below, an agent chosen from the New Conversation pop-up menu in the toolbar, and a file open in the source editor on the right with a preview in the canvas.](https://developer.apple.com/tutorials/images/com.apple.Xcode/coding-assistant-start-conversation@2x.png)

To start a conversation from anywhere in your project using the current agent, click the New Conversation button in the middle of the project window toolbar and enter a prompt in the popover.

Xcode adds a New Conversation to the list in the conversation sidebar. Select the conversation to show the transcript on the right with the message text field at the bottom.

To show or hide the conversation sidebar from anywhere in your project, click the Coding Assistant button.

To start conversations in the source editor, see [Using coding intelligence in the source editor](./using-coding-intelligence-in-the-source-editor.md).

## Enter prompts in the message text field

Enter your prompts in the message text field at the bottom of the transcript. If you start a new conversation, you can click one of the suggested prompts. Xcode changes the name of the conversation to the first prompt.

For example, give Xcode specific instructions on how to generate or modify your code. If you aren’t getting results that you expect, try breaking down your question or adding more detailed instructions.

Although Xcode automatically gathers relevant context based on your prompt and the conversation history, you can also add explicit context to prompts.

To reference specific symbols and files in your project, type the `@` character and choose a symbol or file:

![A screenshot that shows the Project navigator in the sidebar, a source file open in the editor on the right, and a New Conversation popover in the toolbar. There’s an at-character in the message text field, and a completion menu shows suggested symbols and filenames the person can use.](https://developer.apple.com/tutorials/images/com.apple.Xcode/coding-assistant-enter-symbols@2x.png)

To add files for context, inside and outside your project, choose “Add content from project” or “Upload files” from the Attachments pop-up menu in the lower-left corner.

Use other buttons in the message text field to manage a request:

- To submit a prompt that you type, press Return or click the Submit button in the lower-right corner.
- To stop Xcode from responding to a prompt, click the Stop button the lower-right corner.
- To switch models for the agent, choose a model from the Model pop-up menu in the lower-left corner.

Xcode shows whether a conversation is active or waiting for input under the title in the sidebar. You can start multiple conversations and switch between them in the sidebar without losing context.

To undo changes that Xcode makes after responding to a prompt, roll back changes using the history or discard changes using source control.

## Review responses in the transcript

When you submit a prompt, Xcode appends it to the transcript above the message text field and the Jump to Next Active Conversation button in the project window toolbar starts spinning. You can watch the progress in the transcript or do other tasks in the project window while you wait. To quickly jump to the transcript from anywhere in your project, click the Jump to Next Active Conversation button.

Xcode may iterate on a response, build your app to verify the code, and fix build warnings and errors automatically. If the Jump to Next Active Conversation button shows a warning icon, Xcode needs you to perform some action or answer a question in the transcript before continuing. Xcode may ask whether it can use a command-line tool to perform a task. If Xcode needs you to make a decision to proceed, a question and answer interface appears in the transcript.

When Xcode finishes a response, the Jump to Next Active Conversation button stops spinning and Xcode stops updating the transcript.  Review the response in the transcript, because it may contain content that you can interact with. For example, if a response references a filename, click the arrow button next to the filename to open it in the source editor where Xcode uses change bars to highlight any changes to your code. To see more details, choose Verbose from the Adjust Editor Options button pop-up menu on the right of the toolbar.

![A screenshot that shows the conversation list in the sidebar with a conversation selected, a transcript showing a response in the middle, and a file comparison view in the artifacts pane on the right.](https://developer.apple.com/tutorials/images/com.apple.Xcode/coding-assistant-write-code@2x.png)

At the end of the transcript, Xcode may ask you follow-up questions or suggest next steps. You can either answer the questions or enter a new prompt in the same thread. Xcode appends all your prompts, dialogs, and responses to the transcript so that you have a complete record of your conversation. To start a new conversation with a fresh transcript, click the New Conversation button in the toolbar.

To navigate quickly between conversations, use the jump bar in the toolbar or select the conversation in the sidebar. To show the transcript, choose Show Transcript from the Adjust Editor Options button pop-up menu.

For more information on giving agents more tools, including managing permissions you grant in the transcript, see [Extending and customizing agents](./extending-and-customizing-agents.md).

## View project changes in the artifacts pane

Any changes that Xcode makes to your project files using intelligence appear in the artifacts pane on the right or below the transcript.

A comparison view or preview appears for each file that Xcode adds or modifies in your project. In a comparison view, the summary of changes to a file appears to the right of the filename. Similar to the source editor, the artifacts pane shows multicolor change bars to highlight changes Xcode made to the file. To show or hide a file, click the disclosure triangle on the left of the filename.

To add annotations to files, hover the pointer over a file and click the `@` symbol that appears. For code, hover the pointer over a line number. Then type your prompt in the dialog and press Return or click the checkmark in the lower-right corner. Xcode adds the prompt, with the filename and line number reference, to the message text field in the transcript. Add one or more annotations and click the Submit button in the lower-right corner of the message text field.

![A screenshot that shows the conversation list in the sidebar, a transcript in the middle, and a file comparison view in the artifacts pane on the right. There’s an ](https://developer.apple.com/tutorials/images/com.apple.Xcode/coding-assistant-artifacts-pane@2x.png)

To jump to a file in the source editor from the artifacts pane, double-click the filename.

To show the artifacts pane, choose Show Artifacts from the Adjust Editor Options button pop-up menu. To see all the artifacts within a conversation (not just the last response), choose Scope > All Turns under Artifacts from the Adjust Editor Options button pop-up menu.

## Apply changes to your code when you’re ready

To iterate on a software design and approve it before Xcode modifies any code, use plan mode. Xcode proposes changes to your code in the artifacts pane instead of applying them to your code.

To enter plan mode, enter `/plan` at the beginning of your prompt in the transcript message text field. Then review the suggested changes to your project in the artifacts pane.

![A screenshot that shows the conversation sidebar on the left, a transcript in the middle, and a plan in the artifacts pane on the right.](https://developer.apple.com/tutorials/images/com.apple.Xcode/coding-assistant-plan-mode@2x.png)

Optionally, iterate on a solution and approve the changes:

- To add annotations to the plan, hover the pointer over the file, click the `@` symbol that appears and enter your prompt in the dialog that appears. Then click the Submit button in the message text field.
- To apply proposed changes, click Yes in the “Implement the plan?” dialog at the bottom of the transcript.
- To exit plan mode, enter `/exit-plan` in the message text field below.

For more information about plan mode, see [Xcode, agents, and you](https://developer.apple.com/videos/play/wwdc2026/259).

## Roll back changes using the conversation history

Use the conversation history that Xcode maintains to rollback changes to a known state of your project, or to review changes across multiple files in your project.

To roll back changes in a conversation by prompt, choose the conversation in the conversation sidebar. Then choose History from the Adjust Editor Options button pop-up menu. Xcode shows a chronological list of your prompts with a slider on the right.

Move the slider from the bottom to the top to unwind changes in the order that you made them. Move the slider up to remove changes and move the slider down to add changes in the next prompt. To update your project files to the current state of the slider, click the Restore button; otherwise, click Cancel.

![A screenshot that shows the conversation sidebar on the left, the History view with the slider on the right with Cancel and Restore buttons below, and a file comparison view in the artifacts pane on the right.](https://developer.apple.com/tutorials/images/com.apple.Xcode/coding-assistant-history-view@2x.png)

Xcode keeps all the edits in the conversation history in case you decide to reapply changes from subsequent prompts later.

To hide the conversation history, choose Dismiss History from the Adjust Editor Options button pop-up menu.

> **Note**: To use the History feature, your project must have a Git repository. If you don’t have a repository, click the Create Repository button that appears when you click the History button.

## Organize conversations into groups

To find the conversations that you have with agents more easily, rename them appropriately and organize them into groups. For example, you can create a new conversation for each part of a feature you’re working on and create a group for each feature of your app.

Actions you can perform on conversations:

- To start a new conversation, click the New Conversation button and choose an agent from the pop-up menu.
- To show the transcript for a conversation, select it in the conversation sidebar.
- To change the name of a conversation, choose Rename Conversation from the Adjust Editor Options button pop-up menu.
- To hide one or more conversations (use Command-click to select multiple conversations), drag them to the Archive folder at the bottom of the conversation sidebar.
- To delete one or more conversations, select them and press Delete.

Actions you can perform on groups:

- To create a group, click New Group in the conversation sidebar toolbar.
- To change the name of a group, double-click it and enter a name.
- To arrange conversations in groups, drag them to the groups and in the order you want them.
- To collapse groups, click the disclosure triangle to the left of the group.

To explore more conversation and group actions, Control-click one or more conversations or groups, and choose an option from the contextual menu.

## See Also

### Related Documentation
- [Localizing your app using agents](./localizing-your-app-using-agents.md)
  Use agentic coding tools to translate the strings in your app into multiple languages and regions.
### Essentials
- [Setting up coding intelligence](./setting-up-coding-intelligence.md)
  Enable intelligence tools that you want to use in Xcode.
- [Using coding intelligence in the source editor](./using-coding-intelligence-in-the-source-editor.md)
  Submit prompts in the same place you want to make changes to your code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/writing-code-with-intelligence-in-xcode)*