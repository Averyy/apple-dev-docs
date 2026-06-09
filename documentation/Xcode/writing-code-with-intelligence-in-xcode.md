# Writing code with intelligence in Xcode

**Framework**: Xcode

Start conversations with an agent or model in Xcode to generate code, navigate unfamiliar codebases, and fix or refactor existing code.

#### Overview

You interact with an agent or large language model of your choice by entering a series of natural language prompts to ask questions and give instructions. The agent or model refines its responses to your prompts based on previous interactions and any project context that you give it. Xcode presents the responses and changes that it makes to your project files for your review. You can enter another prompt, undo changes, or later, roll back changes to a previous state. Xcode preserves all your interactions in conversations that you can refer to and organize into groups.

You can access Xcode intelligence from anywhere in your project and it blends seamlessly into your workspace. The conversation sidebar behaves like the Project navigator. You can layout and create tabs for the transcript and artifacts panes, similar to editor panes. You can arrange your workspace to run multiple agents in parallel while editing files in another pane.

![A screenshot of the project window with the conversation sidebar on the left, a transcript in the middle with a message text field below, and the artifacts pane on the right.](https://docs-assets.developer.apple.com/published/a29e305b85b67458132b62f223be61c3/coding-assistant-anatomy%402x.png)

Before you begin, set up an agent or model in Intelligence settings and choose it in the coding assistant sidebar. For more information, see [`Setting up coding intelligence`](setting-up-coding-intelligence.md).

#### Start Conversations with an Agent or Model

After you enable one or more agents and chat models, you can start conversations in different places in your project where it’s most convenient for you.

- To start a conversation with a specific agent or model, click the Coding Assistant button or press Command-0. Then click New Conversation in the conversation sidebar, and choose an agent under Agents or a model under Chat in the pop-up menu.
- To start a conversation from anywhere in your project using the current agent or model, click the New Conversation button in the project window toolbar.

![A screenshot that shows the Coding Assistant button selected, the conversation list in the sidebar, an agent chosen from the New Conversation pop-up menu in the toolbar, and a file open in the source editor on the right.](https://docs-assets.developer.apple.com/published/3cdbd6c44b3a646262a094a6b745559d/coding-assistant-start-conversation%402x.png)

Xcode adds a New Conversation to the list in the conversation sidebar and shows the transcript on the right with a message text field at the bottom. The placeholder text shows the current agent or model that Xcode is using. To switch the agent or model, press Command-0 and choose another from the New Conversation pop-up menu.

To show or hide the conversation sidebar from anywhere in your project, click the Coding Assistant button. To start conversations in the source editor, see [`Using coding intelligence in the source editor`](using-coding-intelligence-in-the-source-editor.md).

#### Enter Prompts in the Message Text Field

Enter your prompts in the message text field at the bottom of the transcript or click one of the suggested prompts. If you start a new conversation, Xcode changes the name of the conversation to the first prompt that you enter.

For example, give Xcode specific instructions on how to generate or modify your code. If you aren’t getting results that you expect, try breaking down your question or adding more detailed instructions.

Although Xcode automatically gathers relevant context based on your prompt and the conversation history, you can also add explicit context to prompts.

- To reference specific symbols and files in your project, type the `@` character and choose a symbol or file.
- To add files for context, inside and outside your project, choose “Add context from project” or “Upload files” from the Attachments pop-up menu in the lower-left corner.

![A screenshot that shows the Project navigator in the sidebar, a New Conversation transcript in the editor area. There’s an at-character in the message text field, and a completion menu shows suggested symbols and filenames the person can use.](https://docs-assets.developer.apple.com/published/ed3b81af16fdb5db1fee7472611adda6/coding-assistant-enter-symbols%402x.png)

Use other buttons in the message text field to manage a request:

- To submit a prompt that you type, press Return or click the Submit button in the lower-right corner.
- To stop Xcode from responding to a prompt, click the Stop button the lower-right corner.
- To undo changes that Xcode makes after responding to a prompt, click the Undo Changes button.

If you use a chat product, a Project Context button appears in the lower-left corner of the message text field and is on by default. This allows Xcode to share relevant code and other context from your project with the model. To narrow the scope of the project files, you can turn off the automatic search feature and add explicit references to files and symbols in your prompt instead.

#### Review Responses in the Transcript

When you submit a prompt, Xcode appends it to the transcript above the message text field and the Assistant Activity button in the project window toolbar starts spinning. You can watch the progress in the transcript or do other tasks in the project window while you wait. When a response finishes, the Assistant Activity button stops spinning and Xcode stops updating the transcript. To quickly jump to the transcript from anywhere in your project, click the Assistant Activity button.

Review the response in the transcript, because it may contain content that you can interact with. For example, if a response references a filename, click the arrow button next to the filename to open it in the source editor where Xcode uses multicolor change bars to highlight any changes to your code.

![A screenshot that shows the conversation sidebar on the left, a transcript showing a response in the middle, and a changes to a file in the artifacts pane on the right.](https://docs-assets.developer.apple.com/published/026e6ab9344f5cb0e540732551650afc/coding-assistant-write-code%402x.png)

At the end of the transcript, Xcode may ask you follow-up questions or suggest next steps. You can either answer the questions or enter a new prompt in the same thread. Xcode appends all your prompts, dialogs, and responses to the transcript so that you have a complete record of your conversation. To start a new conversation with a fresh transcript, click the New Conversation button in the toolbar.

If you use an agent, Xcode may iterate on a response, build your app to verify the code, and fix build warnings and errors automatically. If the Assistant Activity button shows a warning icon, Xcode needs you to perform some action or answer a question in the transcript before continuing. For example, Xcode may ask whether it can use a command-line tool to perform a task. If Xcode needs you to make a decision to proceed, a question and answer interface might appear in the transcript.

To navigate quickly between conversations, use the jump bar in the toolbar or select the conversation in the sidebar. To show or hide the transcript, choose Show Transcript from the filter button pop-up menu.

For more information on giving agents more tools, including managing permissions you grant in the transcript, see [`Extending and customizing agents`](extending-and-customizing-agents.md).

#### View Project Changes in the Artifacts Pane

Any changes that Xcode makes to your project files using intelligence appear in the artifacts pane on the right or below the transcript.

A comparison view or preview appears for each file that Xcode adds or modifies in your project. In a comparison view, the summary of changes to a file appears to the right of the filename. Similar to the source editor, the artifacts pane shows multicolor change bars to highlight changes Xcode made to the file. To show or hide a file, click the disclosure triangle on the left of the filename.

To add annotations to the code where you want to make edits, hover the pointer over a line number and click the `@` symbol that appears. Then type your prompt in the dialog and press Return or click the checkmark in the lower-right corner. Xcode adds the prompt, with the filename and line number reference, to the message text field in the transcript. Add one or more annotations and click the Submit button in the lower-right corner of the message text field.

To jump to a file in the source editor from the artifacts pane, double-click the filename, or to show or hide the artifacts pane, choose Show Artifacts from the filter button pop-up menu.

#### Apply Changes to Your Code When You Are Ready

If you use an agent, you can enter plan mode to iterate on a software design and approve it before Xcode modifies any code.

If you use a chat product, you control whether Xcode modifies your project in the message text field before you submit a prompt. If you turn the “Automatically apply code changes” button off, Xcode proposes changes to your code instead of applying them and labels them as “Proposal” in the transcript. The response may contain proposed code that you can selectively apply or paste into your files.

![A screenshot that shows the conversation sidebar on the left and a transcript on the right containing a proposed change in a response.](https://docs-assets.developer.apple.com/published/1b90efc660e1949a20691f110b8ee034/coding-assistant-propose-code%402x.png)

To apply a proposed change, click the code snippet in the response and click Apply in the dialog that appears. If the change adds a new file, click Create New File in the dialog.

#### Roll Back Changes Using the Conversation History

Use the conversation history that Xcode maintains to rollback changes to a known state of your project, or to review changes across multiple files in your project.

To roll back changes in a conversation by prompt, choose the conversation in the conversation sidebar. Then choose History from the More button in the toolbar above the transcript or artifacts pane. Xcode shows a chronological list of your prompts with a slider on the right.

Move the slider from the bottom to the top to unwind changes in the order that you made them. Move the slider up to remove changes and move the slider down to add changes in the next prompt. To update your project files to the current state of the slider, click the Restore button; otherwise, click Cancel.

![A screenshot that shows the conversation sidebar on the left, the History view in the middle with the slider on the right, and the Cancel and Restore buttons below. The changes for the current state are in the artifacts pane on the right.](https://docs-assets.developer.apple.com/published/ba670b3b9f0aa77973c50ea524a44b67/coding-assistant-history-view%402x.png)

Xcode keeps all the edits in the conversation history in case you decide to reapply changes from subsequent prompts later.

To hide the conversation history, choose Dismiss History from the More button in the toolbar above the transcript or artifacts pane.

> **Note**: To use the History feature, your project must have a Git repository. If you don’t have a repository, click the Create Repository button that appears when you click the History button.

#### Organize Conversations Into Groups

To find the conversations that you have with agents and chat models more easily, rename them appropriately and organize them into groups. For example, you can create a new conversation for each part of a feature you’re working on and create a group for each feature of your app.

Actions you can perform on conversations:

- To start a new conversation, click the New Conversation button in the toolbar and choose an agent or model.
- To show the transcript for a conversation, select it in the conversation sidebar.
- To change the name of a conversation, choose Rename Conversation from the More pop-up menu in the toolbar above the transcript or artifacts pane.
- To hide a conversation, drag it to the existing Archive folder at the bottom of the conversation sidebar.

Actions you can perform on groups:

- To create a group, click New Group in the conversation sidebar toolbar.
- To change the name of a group, double-click it and enter a name.
- To arrange conversations in groups, drag them to the groups and in the order you want them.
- To collapse groups, click the disclosure triangle to the left of the group.

To explore more conversation and group actions, Control-click a conversation or group and choose an option from the contextual menu.

## See Also

- [Localizing your app using agents](localizing-your-app-using-agents.md)
  Use agentic coding tools to translate the strings in your app into multiple languages and regions.
- [Setting up coding intelligence](setting-up-coding-intelligence.md)
  Enable intelligence tools that you want to use in Xcode.
- [Using coding intelligence in the source editor](using-coding-intelligence-in-the-source-editor.md)
  Submit prompts in the same place you want to make changes to your code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/writing-code-with-intelligence-in-xcode)*