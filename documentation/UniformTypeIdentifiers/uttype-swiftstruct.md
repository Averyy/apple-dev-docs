# UTType

**Framework**: Uniform Type Identifiers  
**Kind**: struct

A structure that represents a type of data to load, send, or receive.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
struct UTType
```

#### Overview

The [`UTType`](uttype-swift.struct.md) instance may represent files on disk, abstract data types with no on-disk representation, or entirely unrelated hierarchical classification systems, such as hardware. Each instance has a unique [`identifier`](uttype-swift.struct/identifier.md), and helpful properties, such as [`preferredFilenameExtension`](uttype-swift.struct/preferredfilenameextension.md) and [`preferredMIMEType`](uttype-swift.struct/preferredmimetype.md).

> **Note**:  The system includes static declarations for many common types, which you can look up by identifier, filename extension, or MIME type.

A [`UTType`](uttype-swift.struct.md) instance may provide additional information related to the type. For example, it may include a localized user-facing description, a reference URL to technical documentation about the type, or its version number. You can look up types by their conformance to get either a type or a list of types that are relevant to your use case.

To define your own types in your app’s `Info.plist`, see [`Defining file and data types for your app`](defining-file-and-data-types-for-your-app.md).

## Topics

### Looking up a type
- [static func types(tag: String, tagClass: UTTagClass, conformingTo: UTType?) -> [UTType]](uttype-swift.struct/types(tag:tagclass:conformingto:).md)
  Returns an array of types from the provided tag and tag class.
### Creating a type
- [init?(String)](uttype-swift.struct/init(_:).md)
  Creates a type based on an identifier.
- [init?(mimeType: String, conformingTo: UTType)](uttype-swift.struct/init(mimetype:conformingto:).md)
  Creates a type based on a MIME type and a supertype that it conforms to.
- [init?(filenameExtension: String, conformingTo: UTType)](uttype-swift.struct/init(filenameextension:conformingto:).md)
  Creates a type based on a filename extension and an existing supertype that it conforms to.
- [init?(tag: String, tagClass: UTTagClass, conformingTo: UTType?)](uttype-swift.struct/init(tag:tagclass:conformingto:).md)
  Creates a type based on a tag, a tag class, and a supertype that it conforms to.
- [init(exportedAs: String, conformingTo: UTType?)](uttype-swift.struct/init(exportedas:conformingto:).md)
  Creates a type your app owns based on an identifier and a supertype that it conforms to.
- [init(importedAs: String, conformingTo: UTType?)](uttype-swift.struct/init(importedas:conformingto:).md)
  Creates a type your app uses, but doesn’t own, based on an identifier and a supertype that it conforms to.
### Identifying a type
- [typealias ReferenceType](uttype-swift.struct/referencetype.md)
  An alias for the associated reference type.
- [var identifier: String](uttype-swift.struct/identifier.md)
  The string that represents the type.
### Obtaining tags
- [var preferredFilenameExtension: String?](uttype-swift.struct/preferredfilenameextension.md)
  The preferred filename extension for the type.
- [var preferredMIMEType: String?](uttype-swift.struct/preferredmimetype.md)
  The preferred MIME type for the type.
- [var tags: [UTTagClass : [String]]](uttype-swift.struct/tags.md)
  The tag specification dictionary of the type.
### Obtaining additional type information
- [var isDeclared: Bool](uttype-swift.struct/isdeclared.md)
  A Boolean value that indicates whether the system declares the type.
- [var isDynamic: Bool](uttype-swift.struct/isdynamic.md)
  A Boolean value that indicates whether the system generates the type.
- [var isPublic: Bool](uttype-swift.struct/ispublic.md)
  A Boolean value that indicates whether the type is in the public domain.
- [var referenceURL: URL?](uttype-swift.struct/referenceurl.md)
  The reference URL for the type.
- [var version: Int?](uttype-swift.struct/version.md)
  The type’s version, if available.
### Checking a type’s relationship to another type
- [var supertypes: Set<UTType>](uttype-swift.struct/supertypes.md)
  The set of types the type directly or indirectly conforms to.
- [func conforms(to: UTType) -> Bool](uttype-swift.struct/conforms(to:).md)
  Returns a Boolean value that indicates whether a type conforms to the type.
- [func isSubtype(of: UTType) -> Bool](uttype-swift.struct/issubtype(of:).md)
  Returns a Boolean value that indicates whether a type is higher in a hierarchy than the type.
- [func isSupertype(of: UTType) -> Bool](uttype-swift.struct/issupertype(of:).md)
  Returns a Boolean value that indicates whether a type is lower in a hierarchy than the type.
- [Navigating Hierarchical Data Using Outline and Split Views](../AppKit/navigating-hierarchical-data-using-outline-and-split-views.md)
  Build a structured user interface that simplifies navigation in your app.
### Describing a type
- [var localizedDescription: String?](uttype-swift.struct/localizeddescription.md)
  A localized description of the type.
### 3D content
- [static var threeDContent: UTType](uttype-swift.struct/threedcontent.md)
  A base type that represents 3D content.
- [static var usd: UTType](uttype-swift.struct/usd.md)
  A type that represents Universal Scene Description content.
- [static var usdz: UTType](uttype-swift.struct/usdz.md)
  A type that represents Universal Scene Description Package content.
### Apple 3D content
- [static var realityFile: UTType](uttype-swift.struct/realityfile.md)
  A type that represents a Reality Composer file.
- [static var sceneKitScene: UTType](uttype-swift.struct/scenekitscene.md)
  A type that represents a SceneKit serialized scene.
- [static var arReferenceObject: UTType](uttype-swift.struct/arreferenceobject.md)
  A type that represents an augmented reality reference object.
### Apple file system objects
- [static var directory: UTType](uttype-swift.struct/directory.md)
  A type that represents a file system directory, including packages and folders.
- [static var symbolicLink: UTType](uttype-swift.struct/symboliclink.md)
  A type that represents a symbolic link.
- [static var mountPoint: UTType](uttype-swift.struct/mountpoint.md)
  A type that represents a volume mount point.
- [static var aliasFile: UTType](uttype-swift.struct/aliasfile.md)
  A type that represents an alias file.
- [static var folder: UTType](uttype-swift.struct/folder.md)
  A type that represents a user-browsable directory.
- [static var volume: UTType](uttype-swift.struct/volume.md)
  A type that represents the root folder of a volume or mount point.
- [static var diskImage: UTType](uttype-swift.struct/diskimage.md)
  A type that represents a data item that’s mountable as a volume.
### Apple image formats
- [static var heic: UTType](uttype-swift.struct/heic.md)
  A type that represents High Efficiency Image Coding images.
- [static var heif: UTType](uttype-swift.struct/heif.md)
  A type that represents High Efficiency Image File Format images.
- [static var livePhoto: UTType](uttype-swift.struct/livephoto.md)
  A type that represents Live Photos.
### Apple system types
- [static var framework: UTType](uttype-swift.struct/framework.md)
  A type that represents an Apple framework bundle.
- [static var applicationBundle: UTType](uttype-swift.struct/applicationbundle.md)
  A type that represents a bundled app.
- [static var applicationExtension: UTType](uttype-swift.struct/applicationextension.md)
  A type that represents an app extension.
- [static var spotlightImporter: UTType](uttype-swift.struct/spotlightimporter.md)
  A type that represents a Spotlight metadata importer bundle.
- [static var quickLookGenerator: UTType](uttype-swift.struct/quicklookgenerator.md)
  A type that represents a QuickLook preview generator bundle.
- [static var xpcService: UTType](uttype-swift.struct/xpcservice.md)
  A type that represents an XPC service bundle.
- [static var systemPreferencesPane: UTType](uttype-swift.struct/systempreferencespane.md)
  A type that represents a System Preferences pane.
### Application files
- [static var pdf: UTType](uttype-swift.struct/pdf.md)
  A type that represents Adobe Portable Document Format (PDF) documents.
- [static var rtfd: UTType](uttype-swift.struct/rtfd.md)
  A type that represents Rich Text Format Directory documents.
- [static var flatRTFD: UTType](uttype-swift.struct/flatrtfd.md)
  A type that represents flattened Rich Text Format Directory documents.
- [static var epub: UTType](uttype-swift.struct/epub.md)
  A type that represents data in the electronic publication (EPUB) format.
### Audio
- [static var mp3: UTType](uttype-swift.struct/mp3.md)
  A type that represents MP3 audio.
- [static var aiff: UTType](uttype-swift.struct/aiff.md)
  A type that represents data in AIFF audio format.
- [static var wav: UTType](uttype-swift.struct/wav.md)
  A type that represents data in Microsoft Waveform Audio File Format.
- [static var midi: UTType](uttype-swift.struct/midi.md)
  A type that represents data in MIDI audio format.
- [static var playlist: UTType](uttype-swift.struct/playlist.md)
  A base type that represents a playlist.
- [static var m3uPlaylist: UTType](uttype-swift.struct/m3uplaylist.md)
  A type that represents an M3U or M3U8 playlist.
### Audio and video
- [static var quickTimeMovie: UTType](uttype-swift.struct/quicktimemovie.md)
  A type that represents a QuickTime movie.
- [static var mpeg: UTType](uttype-swift.struct/mpeg.md)
  A type that represents an MPEG-1 or MPEG-2 movie.
- [static var mpeg2Video: UTType](uttype-swift.struct/mpeg2video.md)
  A type that represents an MPEG-2 video.
- [static var mpeg2TransportStream: UTType](uttype-swift.struct/mpeg2transportstream.md)
  A type that represents data in MPEG-2 transport stream movie format.
- [static var mpeg4Movie: UTType](uttype-swift.struct/mpeg4movie.md)
  A type that represents an MPEG-4 movie.
- [static var mpeg4Audio: UTType](uttype-swift.struct/mpeg4audio.md)
  A type that represents an MPEG-4 audio layer file.
- [static var appleProtectedMPEG4Video: UTType](uttype-swift.struct/appleprotectedmpeg4video.md)
  A type that represents data in Apple-protected MPEG-4 format.
- [static var appleProtectedMPEG4Audio: UTType](uttype-swift.struct/appleprotectedmpeg4audio.md)
  A type that represents data in Apple-protected MPEG-4 format.
- [static var avi: UTType](uttype-swift.struct/avi.md)
  A type that represents data in AVI movie format.
### Compiled programming language sources
- [static var assemblyLanguageSource: UTType](uttype-swift.struct/assemblylanguagesource.md)
  A type that represents assembly language source code.
- [static var cHeader: UTType](uttype-swift.struct/cheader.md)
  A type that represents a C header file.
- [static var cSource: UTType](uttype-swift.struct/csource.md)
  A type that represents a C source code file.
- [static var cPlusPlusHeader: UTType](uttype-swift.struct/cplusplusheader.md)
  A type that represents a C++ header file.
- [static var cPlusPlusSource: UTType](uttype-swift.struct/cplusplussource.md)
  A type that represents a C++ source code file.
- [static var objectiveCPlusPlusSource: UTType](uttype-swift.struct/objectivecplusplussource.md)
  A type that represents an Objective-C++ source code file.
- [static var objectiveCSource: UTType](uttype-swift.struct/objectivecsource.md)
  A type that represents an Objective-C source code file.
- [static var swiftSource: UTType](uttype-swift.struct/swiftsource.md)
  A type that represents a Swift source code file.
### Compressed archives
- [static var archive: UTType](uttype-swift.struct/archive.md)
  A base type that represents an archive of files and directories.
- [static var zip: UTType](uttype-swift.struct/zip.md)
  A type that represents a zip archive.
- [static var gzip: UTType](uttype-swift.struct/gzip.md)
  A type that represents a GNU zip archive.
- [static var bz2: UTType](uttype-swift.struct/bz2.md)
  A type that represents a bzip2 archive.
- [static var appleArchive: UTType](uttype-swift.struct/applearchive.md)
  A type that represents an Apple archive of files and directories.
### Cryptographic files
- [static var pkcs12: UTType](uttype-swift.struct/pkcs12.md)
  A type that represents Public Key Cryptography Standard (PKCS) 12 data.
- [static var x509Certificate: UTType](uttype-swift.struct/x509certificate.md)
  A type that represents an X.509 certificate.
### Data interchange formats
- [static var delimitedText: UTType](uttype-swift.struct/delimitedtext.md)
  A base type that represents text containing delimited values.
- [static var commaSeparatedText: UTType](uttype-swift.struct/commaseparatedtext.md)
  A type that represents text containing comma-separated values.
- [static var tabSeparatedText: UTType](uttype-swift.struct/tabseparatedtext.md)
  A type that represents text containing tab-separated values.
- [static var utf8TabSeparatedText: UTType](uttype-swift.struct/utf8tabseparatedtext.md)
  A type that represents UTF-8–encoded text containing tab-separated values.
- [static var rtf: UTType](uttype-swift.struct/rtf.md)
  A type that represents Rich Text Format data.
- [static var xml: UTType](uttype-swift.struct/xml.md)
  A type that represents generic XML data.
- [static var yaml: UTType](uttype-swift.struct/yaml.md)
  A type that represents Yet Another Markup Language data.
- [static var json: UTType](uttype-swift.struct/json.md)
  A type that represents JavaScript Object Notation (JSON) data.
- [static var vCard: UTType](uttype-swift.struct/vcard.md)
  A type that represents a vCard file.
### Executables
- [static var executable: UTType](uttype-swift.struct/executable.md)
  A type that represents an executable.
- [static var unixExecutable: UTType](uttype-swift.struct/unixexecutable.md)
  A type that represents a UNIX executable.
- [static var exe: UTType](uttype-swift.struct/exe.md)
  A type that represents a Windows executable.
### Icon images
- [static var ico: UTType](uttype-swift.struct/ico.md)
  A type that represents Windows icon data.
- [static var icns: UTType](uttype-swift.struct/icns.md)
  A type that represents Apple icon data.
### Images
- [static var png: UTType](uttype-swift.struct/png.md)
  A type that represents a PNG image.
- [static var gif: UTType](uttype-swift.struct/gif.md)
  A type that represents a GIF image.
- [static var jpeg: UTType](uttype-swift.struct/jpeg.md)
  A type that represents a JPEG image.
- [static var webP: UTType](uttype-swift.struct/webp.md)
  A type that represents a WebP image.
- [static var tiff: UTType](uttype-swift.struct/tiff.md)
  A type that represents a TIFF image.
- [static var bmp: UTType](uttype-swift.struct/bmp.md)
  A type that represents a Windows bitmap image.
- [static var svg: UTType](uttype-swift.struct/svg.md)
  A type that represents a scalable vector graphics (SVG) image.
- [static var rawImage: UTType](uttype-swift.struct/rawimage.md)
  A base type that represents a raw image format that you use in digital photography.
### Internet-specific
- [static var html: UTType](uttype-swift.struct/html.md)
  A type that represents any version of HTML.
- [static var webArchive: UTType](uttype-swift.struct/webarchive.md)
  A type that represents WebKit web archive data.
- [static var internetLocation: UTType](uttype-swift.struct/internetlocation.md)
  A base type that represents an Apple internet location file.
- [static var internetShortcut: UTType](uttype-swift.struct/internetshortcut.md)
  A type that represents a Microsoft internet shortcut file.
### Property lists
- [static var propertyList: UTType](uttype-swift.struct/propertylist.md)
  A base type that represents a property list.
- [static var xmlPropertyList: UTType](uttype-swift.struct/xmlpropertylist.md)
  A type that represents an XML property list.
- [static var binaryPropertyList: UTType](uttype-swift.struct/binarypropertylist.md)
  A type that represents a binary property list.
### Shazam
- [static var shazamSignature: UTType](uttype-swift.struct/shazamsignature.md)
  A type that represents a signature.
- [static var shazamCustomCatalog: UTType](uttype-swift.struct/shazamcustomcatalog.md)
  A type that represents a custom catalog.
### Scripted programming language sources
- [static var script: UTType](uttype-swift.struct/script.md)
  A base type that represents any scripting language source.
- [static var appleScript: UTType](uttype-swift.struct/applescript.md)
  A type that represents an AppleScript text-based script.
- [static var javaScript: UTType](uttype-swift.struct/javascript.md)
  A type that represents JavaScript source code.
- [static var osaScript: UTType](uttype-swift.struct/osascript.md)
  A type that represents an Open Scripting Architecture binary script.
- [static var osaScriptBundle: UTType](uttype-swift.struct/osascriptbundle.md)
  A type that represents an Open Scripting Architecture script bundle.
- [static var makefile: UTType](uttype-swift.struct/makefile.md)
  A type that represents a Makefile.
- [static var shellScript: UTType](uttype-swift.struct/shellscript.md)
  A base type that represents a shell script.
- [static var pythonScript: UTType](uttype-swift.struct/pythonscript.md)
  A type that represents a Python script.
- [static var rubyScript: UTType](uttype-swift.struct/rubyscript.md)
  A type that represents a Ruby script.
- [static var perlScript: UTType](uttype-swift.struct/perlscript.md)
  A type that represents a Perl script.
- [static var phpScript: UTType](uttype-swift.struct/phpscript.md)
  A type that represents a PHP script.
### Text files
- [static var text: UTType](uttype-swift.struct/text.md)
  A base type that represents all text-encoded data, including text with markup.
- [static var plainText: UTType](uttype-swift.struct/plaintext.md)
  A type that represents text with no markup and an unspecified encoding.
- [static var utf8PlainText: UTType](uttype-swift.struct/utf8plaintext.md)
  A type that represents plain text encoded as UTF-8.
- [static var utf16PlainText: UTType](uttype-swift.struct/utf16plaintext.md)
  A type that represents plain text encoded as UTF-16 in native byte order with an optional bill of materials.
- [static var utf16ExternalPlainText: UTType](uttype-swift.struct/utf16externalplaintext.md)
  A type that represents plain text encoded as UTF-16 with an optional bill of materials.
### URLs
- [static var url: UTType](uttype-swift.struct/url.md)
  A type that represents a URL.
- [static var fileURL: UTType](uttype-swift.struct/fileurl.md)
  A type that represents a URL to a file in the file system.
- [static var urlBookmarkData: UTType](uttype-swift.struct/urlbookmarkdata.md)
  A type that represents a URL bookmark.
### Apple system base types
- [static var item: UTType](uttype-swift.struct/item.md)
  A generic base type for most objects, such as files or directories.
- [static var content: UTType](uttype-swift.struct/content.md)
  A base type that represents anything containing user-viewable content.
- [static var compositeContent: UTType](uttype-swift.struct/compositecontent.md)
  A base type that represents a content format supporting mixed embedded content.
- [static var data: UTType](uttype-swift.struct/data.md)
  A base type that represents any sort of byte stream, including files and in-memory data.
- [static var resolvable: UTType](uttype-swift.struct/resolvable.md)
  A base type that represents a resolvable reference, including symbolic links and aliases.
- [static var package: UTType](uttype-swift.struct/package.md)
  A base type that represents a packaged directory.
- [static var bundle: UTType](uttype-swift.struct/bundle.md)
  A base type that represents a directory that conforms to one of the bundle layouts.
- [static var pluginBundle: UTType](uttype-swift.struct/pluginbundle.md)
  A base type that represents a bundle-based plug-in.
- [static var application: UTType](uttype-swift.struct/application.md)
  A base type that represents a macOS, iOS, iPadOS, watchOS, and tvOS app.
- [static var sourceCode: UTType](uttype-swift.struct/sourcecode.md)
  A base type that represents source code of any programming language.
- [static var bookmark: UTType](uttype-swift.struct/bookmark.md)
  A base type that represents bookmark data.
- [static var log: UTType](uttype-swift.struct/log.md)
  A base type that represents console log data.
### Application base types
- [static var spreadsheet: UTType](uttype-swift.struct/spreadsheet.md)
  A base type that represents a spreadsheet document.
- [static var presentation: UTType](uttype-swift.struct/presentation.md)
  A base type that represents a presentation document.
- [static var database: UTType](uttype-swift.struct/database.md)
  A base type that represents a database store.
- [static var message: UTType](uttype-swift.struct/message.md)
  A base type that represents a message.
- [static var contact: UTType](uttype-swift.struct/contact.md)
  A base type that represents contact information.
- [static var calendarEvent: UTType](uttype-swift.struct/calendarevent.md)
  A base type that represents a calendar event.
- [static var toDoItem: UTType](uttype-swift.struct/todoitem.md)
  A type that represents a to-do item.
- [static var emailMessage: UTType](uttype-swift.struct/emailmessage.md)
  A type that represents an email message.
- [static var font: UTType](uttype-swift.struct/font.md)
  A base type that represents a font.
### Image, audio, and video base types
- [static var image: UTType](uttype-swift.struct/image.md)
  A base type that represents image data.
- [static var audio: UTType](uttype-swift.struct/audio.md)
  A type that represents audio that doesn’t contain video.
- [static var audiovisualContent: UTType](uttype-swift.struct/audiovisualcontent.md)
  A base type that represents data that contains video content that may or may not also include audio.
- [static var movie: UTType](uttype-swift.struct/movie.md)
  A base type representing media formats that may contain both video and audio.
- [static var video: UTType](uttype-swift.struct/video.md)
  A type that represents video that doesn’t contain audio.
### Type Properties
- [static var ahap: UTType](uttype-swift.struct/ahap.md)
- [static var css: UTType](uttype-swift.struct/css.md)
  Cascading Style Sheets (CSS)
- [static var dng: UTType](uttype-swift.struct/dng.md)
  An Adobe DNG (digital negative) image.
- [static var exr: UTType](uttype-swift.struct/exr.md)
  An EXR image.
- [static var geoJSON: UTType](uttype-swift.struct/geojson.md)
  A GeoJSON file.
- [static var heics: UTType](uttype-swift.struct/heics.md)
  A High Efficiency Image Coding Image Sequence.
- [static var jpegxl: UTType](uttype-swift.struct/jpegxl.md)
  A JPEG-XL encoded image.
- [static var linkPresentationMetadata: UTType](uttype-swift.struct/linkpresentationmetadata.md)
  Serialized LinkPresentation metadata.
- [static let paperkit: UTType](uttype-swift.struct/paperkit.md)
  The UTType for storing paper data.
- [static var tarArchive: UTType](uttype-swift.struct/tararchive.md)
  A tar Archive.
### Default Implementations
- [ReferenceConvertible Implementations](uttype-swift.struct/referenceconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [ReferenceConvertible](../Foundation/ReferenceConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct UTTagClass](uttagclass.md)
  A type that represents tag classes.
- [class UTTypeReference](uttypereference.md)
  An object that represents a type of data to load, send, or receive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct)*