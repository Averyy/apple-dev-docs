# Customizing the Completions in the Shortcut Bar

**Framework**: Swift Playgrounds

Guide learners toward a solution by hiding some symbols and showing others.

#### Overview

You can customize the code completions shown in the shortcut bar by hiding and showing different symbols or sets of symbols. You can change the completions shown while editing any part of the playground page.

The following image shows customized code completion in the Learn to Code 1 playground book. The shortcut bar has been customized to show only four methods instead of all possible completions, such as public symbols from the Swift standard library or the current module.

![Screenshot showing a playground page. The shortcut bar is highlighted; it only shows 4 available completions because other candidates have been hidden.](/images/com.apple.Swift-Playgrounds/customizing-the-completions-in-the-shortcut-bar-1@2x.png)

##### Add Code Completion Comments

Specify the completions you want to show or hide by using the `code-completion` delimiter on a line by itself without any preceding whitespace.

![Diagram that shows the syntax of a code completion delimiter. The first line starts with “//#-code-completion(”, followed by a namespace placeholder, followed by the text “, hide”, followed by a completions placeholder, terminated with “)”. The second line includes the same text, except that “hide” is replaced by “show”. ](/images/com.apple.Swift-Playgrounds/customizing-the-completions-in-the-shortcut-bar-2@2x.png)

Use this delimiter to add or remove a symbol or group of symbols from the list of possible completions. In the first argument, *namespace*, specify the space of possible symbols. In the next argument, specify the action to take: add symbols (*show*) or remove symbols (*hide*) from the list of possible code completions. Some combinations of namespace and action include an optional comma-separated list of completions, such as function names or module names.

You can include many `code-completion` delimiters on a playground page. The list of possible completions that a learner sees in the shortcut bar consists of all of the symbols visible at the current insertion point. The `code-completion` delimiters after the current insertion point don’t take effect until the insertion point is moved to a line below those delimeters in the source editor.

##### Select the Symbol Namespace

Use the *namespace* argument of the `code-completion` delimiter to select the scope of the symbols that you’re showing or hiding. You can use any of the following values to select the symbol namespace:

- **`bookauxiliarymodule`**: Any public symbol from the Swift source files in the `Sources` directory for the book.
- **`chapterauxiliarymodule`**: Any public symbol from the Swift source files in the `Sources` directory for the current chapter.
- **`currentmodule`**: Any public symbol from the current playground page.
- **`description`**: Any public symbol in the comma-separated list of strings. Completions: A list of string literals to match against symbol completions based on the name displayed in the shortcut bar.
- **`everything`**: Any public symbol from any module.
- **`identifier`**: Any public identifier in the comma-separated list of arguments. Completions: A list of identifiers, including function names, punctuation, variables, and any other symbols.
- **`keyword`**: Any keyword in the comma-separated list of arguments. Completions: `for`, `func`, `if`, `let`, `var`, and `while`.
- **`literal`**: Any literal in the comma-separated list of arguments. Completions: `array`, `boolean`, `color`, `dictionary`, `image`, `integer`, `nil`, `string`, and `tuple`.
- **`module`**: Any public symbol in the specified modules. Completions: A list of modules.
- **`pageauxiliarymodule`**: Any public symbol from the Swift source files in the `Sources` directory for the current page.
- **`snippet`**: Any code snippet in the comma-separated list of arguments. Completions: A list of snippet names.

Use a combination of namespaces to select the symbols you want to appear. The example below shows a sequence of code-completion delimiters that hide and show certain symbols.

```swift
//#-code-completion(everything, hide)
//#-code-completion(identifier, show, moveForward(), turnLeft(), collectGem(), toggleSwitch())
//#-code-completion(identifier, hide, turnLeft())
//#-code-completion(identifier, show, turnRight())
//#-code-completion(keyword, for)
```

If you need to disambiguate among overloaded symbols, use the `description` namespace selector instead of the `identifier` namespace selector. The `description` namespace includes type information you can use to select specific overloads.

```swift
//#-code-completion(identifier, show, randomInt(from:to:), turnLock(up:numberOfTimes:)
//#-code-completion(description, show, "randomInt(from: Int, to: Int)", "turnLock(up: Book, numberOfTimes: Int)")
```

## See Also

- [Writing Prose for a Playground Page](writing-prose-for-a-playground-page.md)
  Add comment markers in your Swift code to mark text as prose.
- [Specifying Editable Regions in a Playground Page](specifying-editable-regions-in-a-playground-page.md)
  Guide learning by marking code that learners can change or copy forward.
- [Hiding Code from a Playground Page](hiding-code-from-a-playground-page.md)
  Use special Swift comments to hide code from display but continue to run it.
- [Localizing Code Comments and String Literals](localizing-code-comments-and-string-literals.md)
  In Swift Playgrounds 3.0 and later, mark up code zones to replace them with code that’s localized for the current user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift-playgrounds/customizing-the-completions-in-the-shortcut-bar)*