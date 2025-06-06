# Structuring Content for Swift Playgrounds

**Framework**: Swift Playgrounds

Add content to a playground book by creating new folders and property lists.

#### Overview

Combine playground books, chapters, pages, Swift modules, and cutscenes to provide a logical narrative or instructional structure to your content. For example, you can:

- Use books to package root-level Swift Playgrounds content.
- Use chapters to group pages and cutscenes within a book.
- Use pages to write the primary teaching or exploratory content of the book.
- Use modules to implement live views and provide the APIs learners write code against.
- Provide user-editable modules to give learners a space to store and reuse code.
- Intersperse cutscenes with pages to introduce or summarize concepts.

Each part of a playground book must include a manifest property list that contains metadata and references to shared resources.

> ❗ **Important**: Modules are available starting with Swift Playgrounds 3, and version 6 of the Swift Playgrounds book format. For previous versions, place code in the Sources folder of a book, chapter, or page.

Modules are available starting with Swift Playgrounds 3, and version 6 of the Swift Playgrounds book format. For previous versions, place code in the Sources folder of a book, chapter, or page.

##### Determine Book Level Information

You write key details about a playground book in its `Manifest.plist` file. The [`Swift Playgrounds Author Template`](https://developer.apple.comhttps://developer.apple.com/download/more/?=Swift%20Playgrounds%20Author%20Template) comes with a default manifest that you update with specific details about your book, like its title and the file path for the cover image.

You use the book-level manifest to configure the following properties:

## Topics

### Book Structure
- [Adding a Chapter to a Playground Book](adding-a-chapter-to-a-playground-book.md)
  Create a folder with a manifest that describes the chapter’s name and page order.
- [Adding a Page to a Playground Book](adding-a-page-to-a-playground-book.md)
  Create a subfolder, a manifest file, and a content file.
- [Adding a Cutscene to a Playground Book](adding-a-cutscene-to-a-playground-book.md)
  Create a subfolder, a manifest file, and cutscene metadata.
- [Using Modules to Share Code in a Playground Book](using-modules-to-share-code-in-a-playground-book.md)
  In Swift Playgrounds 3.0 and later, make code available across multiple chapters to teach the value of reusable code.
- [Sharing Resources in a Playground Book](sharing-resources-in-a-playground-book.md)
  Reuse common assets throughout a book to reduce its size.

## See Also

- [Creating and Running a Playground Book](creating-and-running-a-playground-book.md)
  Build a playground book from a template, and run it in Swift Playgrounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift-playgrounds/structuring-content-for-swift-playgrounds)*