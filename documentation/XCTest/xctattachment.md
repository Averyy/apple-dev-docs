# XCTAttachment

**Framework**: XCTest  
**Kind**: class

Data from a test method’s execution, such as a file, image, screenshot, data blob, or ZIP file.

## Declaration

```swift
class XCTAttachment
```

## Mentions

- [Adding Attachments to Tests, Activities, and Issues](adding-attachments-to-tests-activities-and-issues.md)

## Topics

### Creating Attachments from Data
- [convenience init(data: Data)](xctattachment/init(data:).md)
  Creates an attachment containing the provided data payload.
- [convenience init(data: Data, uniformTypeIdentifier: String)](xctattachment/init(data:uniformtypeidentifier:).md)
  Creates an attachment containing the provided data payload, with a custom UTI.
- [init(uniformTypeIdentifier: String?, name: String?, payload: Data?, userInfo: [AnyHashable : Any]?)](xctattachment/init(uniformtypeidentifier:name:payload:userinfo:).md)
  Creates an attachment containing the provided data payload, optionally with a custom UTI, name, and user-provided metadata dictionary.
### Creating Attachments from Files and Folders
- [convenience init(contentsOfFileAtURL: URL)](xctattachment/init(contentsoffileaturl:).md)
  Creates an attachment from the contents of an existing file on disk.
- [convenience init(contentsOfFileAtURL: URL, uniformTypeIdentifier: String)](xctattachment/init(contentsoffileaturl:uniformtypeidentifier:).md)
  Creates an attachment from the contents of an existing file on disk, with a custom UTI.
- [convenience init(compressedContentsOfDirectoryAtURL: URL)](xctattachment/init(compressedcontentsofdirectoryaturl:).md)
  Creates an attachment containing a zipped archive of an existing directory on disk.
### Creating Attachments from Images and Screenshots
- [convenience init(image: UIImage)](xctattachment/init(image:).md)
  Creates an attachment containing a PNG representation of the provided image.
- [convenience init(image: UIImage, quality: XCTAttachment.ImageQuality)](xctattachment/init(image:quality:).md)
  Creates an attachment containing a representation of the provided image at the requested image quality.
- [convenience init(screenshot: XCUIScreenshot)](xctattachment/init(screenshot:).md)
  Creates an attachment containing a PNG representation of the provided screenshot.
- [convenience init(screenshot: XCUIScreenshot, quality: XCTAttachment.ImageQuality)](xctattachment/init(screenshot:quality:).md)
  Creates an attachment containing a representation of the provided screenshot at the requested image quality.
- [class XCUIScreenshot](../xcuiautomation/xcuiscreenshot.md)
  A captured image of a screen, app, or UI element state.
- [XCTAttachment.ImageQuality](xctattachment/imagequality.md)
  Compression quality options for image-based attachments.
### Creating Attachments from Objects
- [convenience init(plistObject: Any)](xctattachment/init(plistobject:).md)
  Creates an attachment from an object that can be represented in an XML property list.
- [convenience init(archivableObject: any NSSecureCoding)](xctattachment/init(archivableobject:).md)
  Creates an attachment from an object that conforms to `NSSecureCoding`.
- [convenience init(archivableObject: any NSSecureCoding, uniformTypeIdentifier: String)](xctattachment/init(archivableobject:uniformtypeidentifier:).md)
  Creates an attachment from an object that conforms to `NSSecureCoding`, with a custom UTI.
### Creating Attachments from Strings
- [convenience init(string: String)](xctattachment/init(string:).md)
  Creates an attachment containing the provided string.
### Setting an Attachment’s Lifetime
- [var lifetime: XCTAttachment.Lifetime](xctattachment/lifetime-swift.property.md)
  Indicates whether the attachment is kept or discarded when its associated test passes.
- [XCTAttachment.Lifetime](xctattachment/lifetime-swift.enum.md)
  The possible lifetime values for a test attachment.
### Attachment Metadata
- [var name: String?](xctattachment/name.md)
  The attachment’s name, or `nil` if the attachment is unnamed.
- [var uniformTypeIdentifier: String](xctattachment/uniformtypeidentifier.md)
  The Uniform Type Identifier (UTI) of the data represented by the attachment.
- [var userInfo: [AnyHashable : Any]?](xctattachment/userinfo.md)
  User-provided metadata associated with the attachment.
### Initializers
- [convenience init(compressedContentsOfDirectory: URL)](xctattachment/init(compressedcontentsofdirectory:).md)
- [convenience init(contentsOfFile: URL)](xctattachment/init(contentsoffile:).md)
- [convenience init(contentsOfFile: URL, uniformTypeIdentifier: String)](xctattachment/init(contentsoffile:uniformtypeidentifier:).md)
### Default Implementations
- [XCTAttachment Implementations](xctattachment/xctattachment-implementations.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [Adding Attachments to Tests, Activities, and Issues](adding-attachments-to-tests-activities-and-issues.md)
  Use attachments to store a test’s output data for later analysis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctattachment)*