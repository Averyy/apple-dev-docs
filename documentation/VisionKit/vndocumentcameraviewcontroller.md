# VNDocumentCameraViewController

**Framework**: VisionKit  
**Kind**: class  
**Role**: Class

An object that presents UI for a camera pass-through that helps people scan physical documents.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class VNDocumentCameraViewController
```

```objc
@interface VNDocumentCameraViewController : UIViewController
```

#### Overview

This class enables a person to scan a physical document, page by page, by tapping a camera interface in the controller’s view. The results of a scan include images, by page number. With the collection of scanned images, your app can create a digital version of the physical document and export the scanned images to PDF.

#### Present a document scanning view controller in Swift

The following Swift code presents the document scanning object and adds it to your view controller hierarchy:

```swift
let documentCameraViewController = VNDocumentCameraViewController()
documentCameraViewController.delegate = self
present(documentCameraViewController, animated: true)
```

#### Present a document scanning view controller in Objective-C

The following Objective-C code presents the document scanning object and adds it to your view controller hierarchy:

```objc
VNDocumentCameraViewController* documentCameraViewController = [[VNDocumentCameraViewController alloc] init];
documentCameraViewController.delegate = self;
[self presentViewController:documentCameraViewController animated:YES completion:nil];
```

## Topics

### Supporting the document camera
- [var delegate: (any VNDocumentCameraViewControllerDelegate)?](./vndocumentcameraviewcontroller/delegate.md)
  The delegate to be notified when the user saves or cancels the document scanner.
- [class var isSupported: Bool](./vndocumentcameraviewcontroller/issupported.md)
  A Boolean variable that indicates whether or not the current device supports document scanning.

## Relationships

### Inherits From
- [UIViewController](../UIKit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSExtensionRequestHandling](../Foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UIContentContainer](../UIKit/uicontentcontainer.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../UIKit/uistaterestoring.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Document scanning through the camera
- [Structuring recognized text on a document](./structuring-recognized-text-on-a-document.md)
  Detect, recognize, and structure text on a business card or receipt using Vision and VisionKit.
- [protocol VNDocumentCameraViewControllerDelegate](./vndocumentcameraviewcontrollerdelegate.md)
  A delegate protocol through which the document camera returns its scanned results.
- [class VNDocumentCameraScan](./vndocumentcamerascan.md)
  A single document scanned in the document camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/vndocumentcameraviewcontroller)*