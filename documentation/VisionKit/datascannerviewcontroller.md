# DataScannerViewController

**Framework**: VisionKit  
**Kind**: class

An object that scans the camera live video for text, data in text, and machine-readable codes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@objc class DataScannerViewController
```

## Mentions

- [Scanning data with the camera](scanning-data-with-the-camera.md)

#### Overview

Use a `DataScannerViewController` object to get input from physical objects that appear in the camera’s live video, such as printed text and QR codes on packages.

Create a data scanner by passing parameters that configure the interface to the [`init(recognizedDataTypes:qualityLevel:recognizesMultipleItems:isHighFrameRateTrackingEnabled:isPinchToZoomEnabled:isGuidanceEnabled:isHighlightingEnabled:)`](datascannerviewcontroller/init(recognizeddatatypes:qualitylevel:recognizesmultipleitems:ishighframeratetrackingenabled:ispinchtozoomenabled:isguidanceenabled:ishighlightingenabled:).md) initializer. Then set its delegate to an object in your app that implements the [`DataScannerViewControllerDelegate`](datascannerviewcontrollerdelegate.md) protocol.

Before presenting the view controller, check whether the data scanner is available using the [`isSupported`](datascannerviewcontroller/issupported.md) and [`isAvailable`](datascannerviewcontroller/isavailable.md) properties. Before you can use the data scanner, you must provide a reason for using the camera (add the [`NSCameraUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSCameraUsageDescription) key to the information property list), and a person must agree when the system dialog first appears.

Then begin data scanning by invoking the [`startScanning()`](datascannerviewcontroller/startscanning().md) method and implement the [`dataScanner(_:didTapOn:)`](datascannerviewcontrollerdelegate/datascanner(_:didtapon:).md) and similar delegate methods to handle user actions. Use the [`RecognizedItem`](recognizeditem.md) parameter passed to these methods to perform data-specific actions. For example, if the item is a QR code, perform an action with its payload string, such as opening a URL in a browser, or calling a phone number.

Alternatively, you can track items that appear in the live video using the asynchronous [`recognizedItems`](datascannerviewcontroller/recognizeditems.md) array.

## Topics

### Handling availability
- [class var isSupported: Bool](datascannerviewcontroller/issupported.md)
  A Boolean value that indicates whether the device supports data scanning.
- [class var isAvailable: Bool](datascannerviewcontroller/isavailable.md)
  A Boolean value that indicates whether a person grants your app access to the camera and doesn’t have any restrictions to using the camera.
- [class var supportedTextRecognitionLanguages: [String]](datascannerviewcontroller/supportedtextrecognitionlanguages.md)
  The identifiers for the languages that the data scanner recognizes.
- [DataScannerViewController.ScanningUnavailable](datascannerviewcontroller/scanningunavailable.md)
  The possible reasons the data scanner is unavailable.
### Creating data scanners
- [init(recognizedDataTypes: Set<DataScannerViewController.RecognizedDataType>, qualityLevel: DataScannerViewController.QualityLevel, recognizesMultipleItems: Bool, isHighFrameRateTrackingEnabled: Bool, isPinchToZoomEnabled: Bool, isGuidanceEnabled: Bool, isHighlightingEnabled: Bool)](datascannerviewcontroller/init(recognizeddatatypes:qualitylevel:recognizesmultipleitems:ishighframeratetrackingenabled:ispinchtozoomenabled:isguidanceenabled:ishighlightingenabled:).md)
  Creates a scanner for finding data, such as text and machine-readable codes, in the camera’s live video.
- [let recognizedDataTypes: Set<DataScannerViewController.RecognizedDataType>](datascannerviewcontroller/recognizeddatatypes.md)
  The types of data that the data scanner identifies in the live video.
- [DataScannerViewController.RecognizedDataType](datascannerviewcontroller/recognizeddatatype.md)
  A type of data that the scanner recognizes.
### Configuring data scanners
- [var delegate: (any DataScannerViewControllerDelegate)?](datascannerviewcontroller/delegate.md)
  The delegate that handles user interaction with items recognized by the data scanner.
- [let qualityLevel: DataScannerViewController.QualityLevel](datascannerviewcontroller/qualitylevel-swift.property.md)
  The resolution that the scanner uses to find data.
- [DataScannerViewController.QualityLevel](datascannerviewcontroller/qualitylevel-swift.enum.md)
  The possible quality levels that the scanner uses to find data.
- [let recognizesMultipleItems: Bool](datascannerviewcontroller/recognizesmultipleitems.md)
  A Boolean value that indicates whether the scanner should identify all items in the live video.
- [let isHighFrameRateTrackingEnabled: Bool](datascannerviewcontroller/ishighframeratetrackingenabled.md)
  A Boolean value that determines the frequency at which the scanner updates the geometry of recognized items.
- [let isPinchToZoomEnabled: Bool](datascannerviewcontroller/ispinchtozoomenabled.md)
  A Boolean value that indicates whether people can use a two-finger pinch-to-zoom gesture.
- [let isGuidanceEnabled: Bool](datascannerviewcontroller/isguidanceenabled.md)
  A Boolean value that indicates whether the scanner provides help to a person when selecting items.
- [let isHighlightingEnabled: Bool](datascannerviewcontroller/ishighlightingenabled.md)
  A Boolean value that indicates whether the scanner displays highlights around recognized items.
### Zooming
- [var zoomFactor: Double](datascannerviewcontroller/zoomfactor.md)
  The zoom factor for the live video in the camera.
- [var minZoomFactor: Double](datascannerviewcontroller/minzoomfactor.md)
  The minimum zoom factor that the camera supports.
- [var maxZoomFactor: Double](datascannerviewcontroller/maxzoomfactor.md)
  The maximum zoom factor that the camera supports.
### Scanning and recognizing items
- [func startScanning() throws](datascannerviewcontroller/startscanning.md)
  Starts scanning the camera’s live video for data.
- [func stopScanning()](datascannerviewcontroller/stopscanning.md)
  Stops scanning the camera’s live video for data.
- [var isScanning: Bool](datascannerviewcontroller/isscanning.md)
  A Boolean value that indicates whether the data scanner is actively looking for items.
- [var recognizedItems: AsyncStream<[RecognizedItem]>](datascannerviewcontroller/recognizeditems.md)
  An asynchronous array of items that the data scanner currently recognizes in the camera’s live video.
### Capturing photos
- [func capturePhoto() async throws -> UIImage](datascannerviewcontroller/capturephoto.md)
  Captures a high-resolution photo of the camera’s live video.
### Customizing the interface
- [var overlayContainerView: UIView](datascannerviewcontroller/overlaycontainerview.md)
  A view that the data scanner displays over its view without interfering with the Live Text interface.
- [var regionOfInterest: CGRect?](datascannerviewcontroller/regionofinterest.md)
  The area of the live video in view coordinates that the data scanner searches for items.
### Responding to view controller events
- [func loadView()](datascannerviewcontroller/loadview.md)
  Creates the view that the controller manages.
- [func viewDidLoad()](datascannerviewcontroller/viewdidload.md)
  Performs some action after the system loads the view into memory.
- [func viewWillAppear(Bool)](datascannerviewcontroller/viewwillappear(_:).md)
  Performs some action before the view appears.
- [func viewDidDisappear(Bool)](datascannerviewcontroller/viewdiddisappear(_:).md)
  Performs some action after the view disappears.
- [func removeFromParent()](datascannerviewcontroller/removefromparent.md)
  Removes the view controller from its parent.
### Enumerations
- [DataScannerViewController.TextContentType](datascannerviewcontroller/textcontenttype.md)
  Types of text that a data scanner recognizes.

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

- [Scanning data with the camera](scanning-data-with-the-camera.md)
  Enable Live Text data scanning of text and codes that appear in the camera’s viewfinder.
- [protocol DataScannerViewControllerDelegate](datascannerviewcontrollerdelegate.md)
  A delegate object that responds when people interact with items that the data scanner recognizes.
- [enum RecognizedItem](recognizeditem.md)
  An item that the data scanner recognizes in the camera’s live video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/datascannerviewcontroller)*