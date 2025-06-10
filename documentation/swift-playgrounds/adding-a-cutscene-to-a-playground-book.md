# Adding a Cutscene to a Playground Book

**Framework**: Swift Playgrounds

Create a subfolder, a manifest file, and cutscene metadata.

#### Overview

You can use cutscenes to show animated explanations or introductions to concepts and scenarios. You place cutscenes alongside playground pages in a chapter.

##### Add a Subfolder to a Chapter Folder

Add a cutscene by creating a new folder inside a chapter folder. The name of the subfolder must end with the suffix .cutscenepage. Cutscene folders require two parts: a manifest property list named `Manifest.plist`, and a PrivateResources folder that contains the HTML content of the cutscene.

##### Add Cutscene Resources

Create cutscenes in Swift Playgrounds by using HTML and any resources that you reference in the HTML. The HTML you write for cutscenes can include CSS, JavaScript, and SVG for animations. Your cutscene can also include media such as images, sound, and video.

Place all of the resources used in a cutscene in its PrivateResources folder.

> ❗ **Important**: To localize a cutscene, enclose the cutscene files in a localization folder, such as en.lproj for English, inside the PrivateResources folder.

##### Add the Cutscene Manifest

In Xcode, create a property list file called `Manifest.plist` in the cutscene subfolder. Choose `File > New > File`, then choose the Property List template from `iOS > Resources`. Use the manifest property list to list a cutscene’s name and to reference the HTML file that defines the cutscene.

The cutscene manifest property list has two keys:

## See Also

- [Adding a Chapter to a Playground Book](adding-a-chapter-to-a-playground-book.md)
  Create a folder with a manifest that describes the chapter’s name and page order.
- [Adding a Page to a Playground Book](adding-a-page-to-a-playground-book.md)
  Create a subfolder, a manifest file, and a content file.
- [Using Modules to Share Code in a Playground Book](using-modules-to-share-code-in-a-playground-book.md)
  In Swift Playgrounds 3.0 and later, make code available across multiple chapters to teach the value of reusable code.
- [Sharing Resources in a Playground Book](sharing-resources-in-a-playground-book.md)
  Reuse common assets throughout a book to reduce its size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift-playgrounds/adding-a-cutscene-to-a-playground-book)*