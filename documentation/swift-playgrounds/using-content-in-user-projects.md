# Importing sample content into user app playgrounds

**Framework**: Swift Playgrounds

Learn how to bring sample code into your app playground.

#### Overview

While using Swift Playgrounds you might discover some code in one of the various samples that you’d like to use in your app. For example, you might find a particular view has a useful layout, or that a model for a particular part of a sample app is similar to what you want in your own app. To bring code from an app playground (`.swiftpm`), it’s helpful to know what you want to bring over. Here are some tips and tricks when it comes to bringing code from Swift Playgrounds samples into your app.

##### Transfer Data Models

Data representation is an important part of app development. For example, designing a class with all the necessary properties and methods ensures easy data passing. In addition, it’s important to consider how you store your data to make sure reading and writing happens quickly to make sure users aren’t waiting. The content in Swift Playgrounds shows a number of different models whether it’s a [`page of a story`](https://developer.apple.comhttps://developer.apple.com/tutorials/sample-apps/chooseyourownstory), and event in a [`date planner`](https://developer.apple.comhttps://developer.apple.com/tutorials/sample-apps/dateplanner), or a panda image used to make a [`meme`](https://developer.apple.comhttps://developer.apple.com/tutorials/sample-apps/memecreator).

The first step in adopting code from another app playground is knowing what code you want to repurpose. For example, if you are making an app showing images available on a different website, you might look at the `Panda` and `PandaCollectionFetcher` objects in [`meme`](https://developer.apple.comhttps://developer.apple.com/tutorials/sample-apps/memecreator) to see what information there is useful to you. You might start by looking at the way the `PandaCollectionFetcher` collects and processes the data.

You might find that data on the website you want to download images from uses a different model than the website used by Meme Creator. For example, assume the website allows you to make database style requests and returns a list of addresses. You would find that the `Panda` and `PandaCollection` objects will work as-is. What does change, however, is the code in the `PandaCollectionFetcher` which you use to make a URL request with a database query, and then a small change to the way you process the data to handle a list instead of a dictionary. With those changes – and some renaming to fit the classes into your app – you can use code from Swift Playgrounds in your app.

##### Transfer Views and View Elements

Views make up the visible portion of your app. Swift Playgrounds shows a number of different concepts for UI that can be used in your app.

The key to finding view code you want to have in your app is to understand what your app needs. For example, if you’ve just completed the Date Planner sample, and you want to employ a list view with different sections, like `EventList`. To do this, it’s best to start by copying the entire view structure that you want to use. After you have that, there are a few more items you’ll needed to bring over:

- Find all of the component views that make up the `EventList`, namely `Period`, `EventRow`, and `EventEditor`. This ensures that you have all of the view code necessary to show the event list.
- Because the adopted code can no longer access the models in an older app playgrounds, remove references to the those models. Do this by either replacing the model references with fake data, or, if your model code is set up and ready for display, you can add references to your model code. After connecting the data to the view, check the preview to see if the view uses the data as expected.
- Make tweaks and small changes as necessary, such as adding modifiers to various views.

These steps work just as well when adopting view code for a component of another view. If the view code consists of SwiftUI built-in views like `HStack`, `Text`, or `Button`, then you need to copy this structure and swap out the model code. If the component view you want consists of other views, follow the above steps and bring all of the component views into your app playground.

## See Also

- [Adding a Swift package to your app playground](add-a-swift-package.md)
  Extend the functionality of your app playground by finding and adding a publicly available Swift package.
- [Debugging an App Playground using the Console](console-print-debugging.md)
  Learn different methods to debug your code using console output.
- [Previewing SwiftUI views in Swift Playgrounds](live-preview.md)
  Use the canvas in Swift Playgrounds to see a live preview of the SwiftUI views in your app.
- [Requesting access to capabilities for your app playground](project-capabilities.md)
  Request access for your app to protected resources, services, or device hardware such as sensors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift-playgrounds/using-content-in-user-projects)*