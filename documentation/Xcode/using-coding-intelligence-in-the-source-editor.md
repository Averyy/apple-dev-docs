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

Enter your prompt in the message text field in the coding tools popover or click one of the buttons, such as Explain, Generate a Preview, or Generate a Playground, depending on the context.

#### Generate Playgrounds and Previews

Playgrounds and previews let you experiment with new code without modifying your app. Use playgrounds to run and display code snippets in the canvas, and use previews to validate UI code across platforms. Xcode generates playground and preview code that may contain sample data to help you understand and visualize the code in the canvas.

To add a playground macro to your project, open the coding tools popover and choose Generate a Playground:

Xcode starts a new conversation with a playground prompt, shows the response in the transcript, and displays the generated playground code in the artifacts pane. To see the code in the source editor, double-click the filename in the artifacts pane. To see the playground in the canvas, click Show Canvas in the toolbar if necessary.

Similarly, with an interface file in the source editor, open the coding tools popover and click Generate a Preview. Xcode adds the generated preview code to your file and renders the preview in the artifacts pane. Click the preview to jump to the code in the source editor.

To learn more about the playground macro, see [`Running code snippets using the playground macro`](running-code-snippets-using-the-playground-macro.md). For previews, see [`Previewing your app’s interface in Xcode`](previewing-your-apps-interface-in-xcode.md).

#### Generate Documentation

Let Xcode draft [`Swift-DocC`](https://developer.apple.comhttps://www.swift.org/documentation/docc/)-style documentation comments above a symbol in a source file.

In the source editor, select a symbol that needs documentation comments, open the coding tools popover, and click Document.

For example, if you select a class, Xcode adds documentation for the class and for its properties and methods, including method parameters. Xcode shows the prompt and the response in the transcript and the changes to the file in the artifacts pane.

To view your documentation in Xcode’s Developer Documentation window, choose Product > Build Documentation.

#### Fix Your Code

If you choose an agent when starting a conversation, Xcode automatically builds your app after editing your code and attempts to fix issues for you. If you encounter a compilation warning or error while building your app, Xcode can often generate a fix for you too.

The source editor highlights any issues with a red or yellow underline and presents an issue summary and icon. Click the icon to show more information about the issue, then click Generate next to “Generate Fix for Issue”. Xcode shows the details for the fix in the transcript and shows the changes in the artifacts pane.

## See Also

- [Writing code with intelligence in Xcode](writing-code-with-intelligence-in-xcode.md)
  Start conversations with an agent or model in Xcode to generate code, navigate unfamiliar codebases, and fix or refactor existing code.
- [Setting up coding intelligence](setting-up-coding-intelligence.md)
  Enable intelligence tools that you want to use in Xcode.
- [Writing code with intelligence in Xcode](writing-code-with-intelligence-in-xcode.md)
  Start conversations with an agent or model in Xcode to generate code, navigate unfamiliar codebases, and fix or refactor existing code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/using-coding-intelligence-in-the-source-editor)*