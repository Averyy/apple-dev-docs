# VNDocumentCameraViewController

**Framework**: VisionKit  
**Kind**: class

An object that presents UI for a camera pass-through that helps people scan physical documents.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class VNDocumentCameraViewController
```

#### Overview

This class enables a person to scan a physical document, page by page, by tapping a camera interface in the controller’s view. The results of a scan include images, by page number. With the collection of scanned images, your app can create a digital version of the physical document and export the scanned images to PDF.

#### Present a Document Scanning View Controller in Swift

The following Swift code presents the document scanning object and adds it to your view controller hierarchy:

```swift
let documentCameraViewController = VNDocumentCameraViewController()
documentCameraViewController.delegate = self
present(documentCameraViewController, animated: true)
```

#### Present a Document Scanning View Controller in Objective C

The following Objective-C code presents the document scanning object and adds it to your view controller hierarchy:

```objc
VNDocumentCameraViewController* documentCameraViewController = [[VNDocumentCameraViewController alloc] init];
documentCameraViewController.delegate = self;
[self presentViewController:documentCameraViewController animated:YES completion:nil];
```

## Topics

### Supporting the document camera
- [var delegate: (any VNDocumentCameraViewControllerDelegate)?](vndocumentcameraviewcontroller/delegate.md)
  The delegate to be notified when the user saves or cancels the document scanner.
- [class var isSupported: Bool](vndocumentcameraviewcontroller/issupported.md)
  A Boolean variable that indicates whether or not the current device supports document scanning.

## Relationships

### Inherits From
- [UIViewController](../UIKit/UIViewController.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UIContentContainer](../UIKit/UIContentContainer.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UIStateRestoring](../UIKit/UIStateRestoring.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [Structuring Recognized Text on a Document](structuring_recognized_text_on_a_document.md)
  Detect, recognize, and structure text on a business card or receipt using Vision and VisionKit.
- [protocol VNDocumentCameraViewControllerDelegate](vndocumentcameraviewcontrollerdelegate.md)
  A delegate protocol through which the document camera returns its scanned results.
- [class VNDocumentCameraScan](vndocumentcamerascan.md)
  A single document scanned in the document camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/vndocumentcameraviewcontroller)*