# Using coding intelligence in the source editor

**Framework**: Xcode  
**Role**: Article

Submit prompts in the same place you want to make changes to your code.

## Overview

You can use coding intelligence in the source editor to submit prompts using the coding tools popover. You can also generate fixes for issues that Xcode detects in your code.

Before you begin, set up one or more agents in Intelligence settings. For more information, see [Setting up coding intelligence](./setting-up-coding-intelligence.md) and [Writing code with intelligence in Xcode](./writing-code-with-intelligence-in-xcode.md).

## Start conversations in the source editor

To display the coding tools popover in the source editor, perform one of these actions:

- Control-click a symbol or code selection and choose Show Coding Tools > Show Coding Tools from the contextual menu.
- Select some code and click the coding assistant button that appears in the source editor gutter.
- Press Command-Option-0 from anywhere in the source editor with or without selecting code.

![A screenshot that shows the Project navigator in the sidebar and the source editor on the right with a code snippet selected and the Show Coding Tools popover displayed with the Explain button.](https://developer.apple.com/tutorials/images/com.apple.Xcode/coding-assistant-show-coding-tools@2x.png)

Enter your prompt in the message text field in the coding tools popover or click one of the buttons, such as Explain, Generate a Preview, or Generate a Playground, depending on the context. Xcode shows the response in the transcript and any content it generates in the artifacts pane.

## Generate playgrounds and previews

Playgrounds and previews let you experiment with new code without modifying your app. Use playgrounds to run and display code snippets in the canvas, and use previews to validate UI code across platforms. Xcode generates playground and preview code that may contain sample data to help you understand and visualize the code in the canvas.

To add a playground macro to your project, open the coding tools popover and click Generate a Playground:

![A screenshot that shows the Project navigator in the sidebar and the source editor on the right with a class selected and the Show Coding Tools popover displayed with the Generate a Playground button.](https://developer.apple.com/tutorials/images/com.apple.Xcode/coding-assistant-generate-playground@2x.png)

Xcode starts a new conversation with a playground prompt, shows the response in the transcript, and displays the generated playground code in the artifacts pane.

To run the playground in the canvas, double-click the filename in the artifacts pane, click Show Canvas in the toolbar, and click the Restart button in the canvas if necessary.

![A screenshot that shows the Project navigator in the sidebar, a file opened in the source editor with the playground code generated, and the playground run in the canvas on the right.](https://developer.apple.com/tutorials/images/com.apple.Xcode/coding-assistant-run-playground@2x.png)

Similarly, with an interface file in the source editor, open the coding tools popover and click Generate a Preview. Xcode adds the generated preview code to your file and you run the preview in the source editor canvas.

For more information, see [Running code snippets using the playground macro](./running-code-snippets-using-the-playground-macro.md) and [Adding previews to your interface files](./adding-previews-to-your-interface-files.md).

## Fix your code

When you use the coding assistant, Xcode automatically builds your app after editing your code and attempts to fix issues for you. If you encounter a compilation warning or error while building your app, Xcode can often generate a fix for you.

The source editor highlights any issues with a red or yellow underline and presents an issue summary and icon. Click the icon to show more information about the issue, then click Generate next to “Generate Fix for Issue”.

Xcode shows the details for the fix in the transcript and shows the changes in the artifacts pane.

![A screenshot that shows the Project navigator on the left, a file open in the source editor on the right, and a Fix-it dialog with an error message and a Generate button.](https://developer.apple.com/tutorials/images/com.apple.Xcode/coding-assistant-generate-fix-it@2x.png)

## See Also

### Related Documentation
- [Writing code with intelligence in Xcode](./writing-code-with-intelligence-in-xcode.md)
  Start conversations with an agent in Xcode to generate code, navigate unfamiliar codebases, and fix or refactor existing code.
### Essentials
- [Setting up coding intelligence](./setting-up-coding-intelligence.md)
  Enable intelligence tools that you want to use in Xcode.
- [Writing code with intelligence in Xcode](./writing-code-with-intelligence-in-xcode.md)
  Start conversations with an agent in Xcode to generate code, navigate unfamiliar codebases, and fix or refactor existing code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/using-coding-intelligence-in-the-source-editor)*