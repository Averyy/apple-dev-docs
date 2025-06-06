# Adding a Page to a Playground Book

**Framework**: Swift Playgrounds

Create a subfolder, a manifest file, and a content file.

#### Overview

Playground pages are the primary content of a playground book. They contain the code, prose, and optional live view that make up the primary Swift Playgrounds interface that’s displayed when viewing a book.

##### Add a Subfolder to a Chapter Folder

Add a page by selecting a chapter folder and adding a subfolder to it. The subfolder’s name must end in the suffix .playgroundpage.

In Xcode, create a property list file called `Manifest.plist` in the new page’s subfolder. Choose File > New > File, then choose the Property List template from iOS > Resources. Use the manifest property list to list the page’s name and configuration metadata.

##### Add Code and Prose

For each page in your playground book, create a `main.swift` file. This file is where you write most of the content—code and prose—that learners see in a playground book. The code and prose you write in this file appears on the left side of a page when it’s displayed in Swift Playgrounds.

> ❗ **Important**: If you’re writing a book that targets a version of the Swift Playgrounds book format earlier than `6.0`, use the name `Contents.swift` instead of `main.swift`.

If you’re writing a book that targets a version of the Swift Playgrounds book format earlier than `6.0`, use the name `Contents.swift` instead of `main.swift`.

By default, everything you write in `main.swift` is treated as normal Swift code that runs when a learner taps the Run button. Playground pages support rich annotions that you use to write prose and add functionality. For more information about annotations, see  and [`Writing Prose for a Playground Page`](writing-prose-for-a-playground-page.md).

##### Add an Always on Live View

To display the results of running the code on a page, you can add an always-on live view. When present, it’s displayed on the right side of a page. Add an always-on live view by creating a file named `LiveView.swift` and placing it in a page’s .playgroundpage folder.

For the view to appear on the page, you must set the [`liveView`](https://developer.apple.com/documentation/playgroundsupport/playgroundpage/1964506-liveview) property of the current page within `LiveView.swift`.

```swift
PlaygroundPage.current.liveView = <# An instance of UIView or UIViewController #>
```

##### Specify the Page Name and Metadata

A page’s manifest property list determines both the page name and metadata for presenting the page in Swift Playgrounds. Configure the following property list keys in the manifest:

## See Also

- [Adding a Chapter to a Playground Book](adding-a-chapter-to-a-playground-book.md)
  Create a folder with a manifest that describes the chapter’s name and page order.
- [Adding a Cutscene to a Playground Book](adding-a-cutscene-to-a-playground-book.md)
  Create a subfolder, a manifest file, and cutscene metadata.
- [Using Modules to Share Code in a Playground Book](using-modules-to-share-code-in-a-playground-book.md)
  In Swift Playgrounds 3.0 and later, make code available across multiple chapters to teach the value of reusable code.
- [Sharing Resources in a Playground Book](sharing-resources-in-a-playground-book.md)
  Reuse common assets throughout a book to reduce its size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift-playgrounds/adding-a-page-to-a-playground-book)*