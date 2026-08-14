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
- [UIViewController](../uikit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UIContentContainer](../uikit/uicontentcontainer.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../uikit/uistaterestoring.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

- [Structuring recognized text on a document](structuring-recognized-text-on-a-document.md)
  Detect, recognize, and structure text on a business card or receipt using Vision and VisionKit.
- [protocol VNDocumentCameraViewControllerDelegate](vndocumentcameraviewcontrollerdelegate.md)
  A delegate protocol through which the document camera returns its scanned results.
- [class VNDocumentCameraScan](vndocumentcamerascan.md)
  A single document scanned in the document camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/vndocumentcameraviewcontroller)*