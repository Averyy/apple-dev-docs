# Using coding intelligence in the source editor

**Framework**: Xcode

Submit prompts in the same place you want to make changes to your code.

#### Overview

You can use coding intelligence in the source editor to submit prompts using the coding tools popover. You can also generate fixes for issues that Xcode detects in your code.

Before you begin, set up an agent or chat provider in Intelligence settings. For more information, see [`Setting up coding intelligence`](setting-up-coding-intelligence.md).

#### Start Conversations in the Source Editor

To display the coding tools popover in the source editor, perform one of these actions:

- Control-click a symbol or code selection and choose Show Coding Tools > Show Coding Tools from the contextual menu.
- Select some code and click the coding assistant button that appears in the source editor gutter.
- Press Command-Option-0 from anywhere in the source editor with or without selecting code.

![A screenshot that shows the Project navigator in the sidebar and the source editor on the right with a code snippet selected and the Show Coding Tools popover displayed with the Explain button.](/images/com.apple.Xcode/coding-assistant-show-coding-tools@2x.png)

Enter your prompt in the message text field in the coding tools popover or click one of the buttons, such as Explain, Generate a Preview, or Generate a Playground, depending on the context.

#### Generate Playgrounds and Previews

Playgrounds and previews let you experiment with new code without modifying your app. Use playgrounds to run and display code snippets in the canvas, and use previews to validate UI code across platforms. Xcode generates playground and preview code that may contain sample data to help you understand and visualize the code in the canvas.

To add a playground macro to your project, open the coding tools popover and click Generate a Playground:

![A screenshot that shows the Project navigator in the sidebar and the source editor on the right with a class selected and the Show Coding Tools popover displayed with the Generate a Playground button.](/images/com.apple.Xcode/coding-assistant-generate-playground@2x.png)

If you use an agent, Xcode starts a new conversation with a playground prompt, shows the response in the transcript, and displays the generated playground code in the artifacts pane. To see the code in the source editor, double-click the filename in the artifacts pane. To run the playground in the canvas, click Show Canvas in the toolbar if necessary.

If you use a chat model, Xcode shows the code changes directly in the source editor and runs the playground in the canvas.

![A screenshot that shows the Project navigator in the sidebar, a file opened in the source editor with the playground code generated, and the playground run in the canvas on the right.](/images/com.apple.Xcode/coding-assistant-run-playground@2x.png)

Similarly, with an interface file in the source editor, open the coding tools popover and click Generate a Preview. Xcode adds the generated preview code to your file and renders the preview in the artifacts pane or the canvas.

For more information, see [`Running code snippets using the playground macro`](running-code-snippets-using-the-playground-macro.md) and [`Previewing your app’s interface in Xcode`](previewing-your-apps-interface-in-xcode.md).

#### Generate Documentation

Let Xcode draft [`Swift-DocC`](https://developer.apple.comhttps://www.swift.org/documentation/docc/)-style documentation comments above a symbol in a source file.

In the source editor, select a symbol that needs documentation comments, open the coding tools popover, and click Document.

For example, if you select a class, Xcode adds documentation for the class and for its properties and methods, including method parameters. For an agent, Xcode shows the prompt in the transcript and the changes to the file in the artifacts pane. For a chat model, Xcode shows the documentation comments directly in the source editor.

![A screenshot of the Project navigator on the left, a file open in the source editor with generated DocC style comments above the structure name.](/images/com.apple.Xcode/coding-assistant-generate-docs@2x.png)

To view your documentation in Xcode’s Developer Documentation window, choose Product > Build Documentation.

#### Fix Your Code

If you choose an agent when starting a conversation, Xcode automatically builds your app after editing your code and attempts to fix issues for you. If you encounter a compilation warning or error while building your app, Xcode can often generate a fix for you too.

The source editor highlights any issues with a red or yellow underline and presents an issue summary and icon. Click the icon to show more information about the issue, then click Generate next to “Generate Fix for Issue”.

For an agent, Xcode shows the details for the fix in the transcript and shows the changes in the artifacts pane. For a chat model, Xcode makes the code changes directly in the source editor.

![A screenshot that shows the Project navigator on the left, a file open in the source editor on the right, and a Fix-it dialog with an error message and a Generate button.](/images/com.apple.Xcode/coding-assistant-generate-fix-it@2x.png)

## See Also

- [Writing code with intelligence in Xcode](writing-code-with-intelligence-in-xcode.md)
  Start conversations with an agent or model in Xcode to generate code, navigate unfamiliar codebases, and fix or refactor existing code.
- [Setting up coding intelligence](setting-up-coding-intelligence.md)
  Enable intelligence tools that you want to use in Xcode.
- [Writing code with intelligence in Xcode](writing-code-with-intelligence-in-xcode.md)
  Start conversations with an agent or model in Xcode to generate code, navigate unfamiliar codebases, and fix or refactor existing code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/using-coding-intelligence-in-the-source-editor)*