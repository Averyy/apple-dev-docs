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

##### Determine Book Level Information

You write key details about a playground book in its `Manifest.plist` file. The [`Swift Playgrounds Author Template`](https://developer.apple.comhttps://developer.apple.com/download/more/?=Swift%20Playgrounds%20Author%20Template) comes with a default manifest that you update with specific details about your book, like its title and the file path for the cover image.

You use the book-level manifest to configure the following properties:

- **`Chapters`**: **Required.** An array of strings you use to order the chapters in a book. Each string is the name of a `.playgroundchapter` directory that contains the content and resources for a chapter.
- **`ContentIdentifier`**: **Required.** A string that uniquely identifies your book among all others. The identifier must be in reverse-DNS format, and you should use a domain that you or your organization controls. For example, if you own `example.com`, you might set a book’s `ContentIdentifier` property to `com.example.mybook`.
- **`ContentVersion`**: **Required.** A string containing the version number of a book. The string can only contain sequences of numbers and periods, such as `2.0.1`. Increment the version of the book when you publish updates to it.
- **`DeploymentTarget`**: **Required.** A string that contains the minimum version of iOS (10.0 or later) required to run your book. You prefix the version number with the string `ios`. For example, the version string for iOS 11.3 is `ios11.3`.
- **`DevelopmentRegion`**: **Required.** The default language and region for the book, as a Language ID. For more information, see [`Language IDs`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/LanguageandLocaleIDs/LanguageandLocaleIDs.html#//apple_ref/doc/uid/10000171i-CH15-SW6) and [`CFBundleDevelopmentRegion`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.html#//apple_ref/doc/uid/20001431-130430).
- **`ImageReference`**: A string containing a reference to a `.png` image file that’s stored in the book’s Resources folder and used as the book icon. The icon must be an image with a 4:3 aspect ratio. The recommended image size is 400 × 300 pixels.
- **`Name`**: **Required.** A string you use to provide a title for a book. This title becomes the learner-facing name displayed in Swift Playgrounds.
- **`Version`**: **Required.** A string containing the version of the Swift Playgrounds book format used to write the book. Use `6.0`.
- **`SwiftVersion`**: A string containing the version of Swift that the playground book uses. The default is `5.0`.
- **`MinimumSwiftPlaygroundsVersion`**: A string containing the minimum version of the Swift Playgrounds app that your book requires. The default is `1.2`.
- **`UserModuleMode`**: **Required.** A string you use to determine the degree to which a learner has control over user-editable modules in the book. The module mode must be one of the following types: `"Full"`—User-editable modules that the user can add and remove as needed. `"Limited"`—A nonremovable user module that you supply with your book. `"Disabled"`—No user-editable modules are available. This property is available starting with Swift Playgrounds 3.

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