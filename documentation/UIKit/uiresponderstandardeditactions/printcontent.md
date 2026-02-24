# printContent(_:)

**Framework**: UIKit  
**Kind**: method

Tells your app to print available content.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
optional func printContent(_ sender: Any?)
```

#### Discussion

Implement this method on the responder responsible for printing the contents of the window scene; for instance, the root view controller of a [`UIWindow`](uiwindow.md). In your implementation, prepare the print job and present an instance of [`UIPrintInteractionController`](uiprintinteractioncontroller.md) to show a Print dialog.

**Swift**:

```swift
override func printContent(_ sender: Any?) {
    let info = UIPrintInfo.printInfo()
    info.outputType = .photo
    info.orientation = .portrait
    info.jobName = modelItem.title
    
    let printInteractionController = UIPrintInteractionController()
    printInteractionController.printInfo = info
    printInteractionController.printingItem = modelItem.image
    
    let completionHandler: UIPrintInteractionController.CompletionHandler = {
        (controller: UIPrintInteractionController, completed: Bool, error: Error?) in
        if let error = error {
            Logger().error("Print failed due to an error: \(error.localizedDescription)")
        }
    }
    
    if traitCollection.userInterfaceIdiom == .pad {
        if let printButton = navigationItem.rightBarButtonItem {
            printInteractionController.present(from: printButton, animated: true, completionHandler: completionHandler)
        }
    } else {
        printInteractionController.present(animated: true, completionHandler: completionHandler)
    }
}
```

**Objective-C**:

```objc
- (void)print:(id)sender {
    UIPrintInfo *info = UIPrintInfo.printInfo;
    info.outputType = UIPrintInfoOutputPhoto;
    info.orientation = UIPrintInfoOrientationPortrait;
    info.jobName = _modelItem.title;
    
    UIPrintInteractionController *printInteractionController = [[UIPrintInteractionController alloc] init];
    printInteractionController.printInfo = info;
    printInteractionController.printingItem = _modelItem.image;
    
    UIPrintInteractionCompletionHandler completionHandler = ^(UIPrintInteractionController *printController, BOOL completed, NSError *error) {
        if (error != nil) {
            NSLog(@"Print failed due to an error in domain %@ with error code %lu.", error.domain, (long)error.code);
        }
    };
    
    if (self.traitCollection.userInterfaceIdiom == UIUserInterfaceIdiomPad) {
        UIBarButtonItem *printButton = self.navigationItem.rightBarButtonItem;
        [printInteractionController presentFromBarButtonItem:printButton animated:YES completionHandler:completionHandler];
    } else {
        [printInteractionController presentAnimated:YES completionHandler: completionHandler];
    }
}
```

If your app includes the [`UIApplicationSupportsPrintCommand`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIApplicationSupportsPrintCommand) key in its `Info.plist` file, people can print from your app using the keyboard shortcut Command-P, which calls [`printContent(_:)`](uiresponderstandardeditactions/printcontent(_:).md). You can also set [`printContent(_:)`](uiresponderstandardeditactions/printcontent(_:).md) as the action on other print-related controls such as a print button on a toolbar.

For more information about printing from your app, see [`Printing`](printing.md).

## Parameters

- `sender`: The object calling this method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions/printcontent(_:))*