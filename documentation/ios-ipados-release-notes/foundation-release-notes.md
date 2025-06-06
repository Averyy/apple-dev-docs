# Foundation Release Notes

**Framework**: iOS & iPadOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

Foundation in macOS 10.14, iOS 12, watchOS 5, and tvOS 12 includes new features, API changes, and deprecations. For information about earlier releases, see [`Foundation Release Notes for macOS 10.13 and iOS 11`](https://developer.apple.comhttps://developer.apple.com/library/archive/releasenotes/Foundation/RN-Foundation/index.html).

##### Secure Data Archival and Unarchival

The [`NSKeyedArchiver`](https://developer.apple.com/documentation/Foundation/NSKeyedArchiver) and [`NSKeyedUnarchiver`](https://developer.apple.com/documentation/Foundation/NSKeyedUnarchiver) classes have new initializers and helper methods that make it easier for you to enable secure coding for archival and unarchival. Each initializer or helper method replaces a corresponding member that’s now deprecated.

- [`init(requiringSecureCoding:)`](https://developer.apple.com/documentation/foundation/nskeyedarchiver/2962881-init) replaces [`init()`](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/2962882-init) and [`init(forWritingWith:)`](https://developer.apple.com/documentation/foundation/nskeyedarchiver/1409579-init).
- [`archivedData(withRootObject:requiringSecureCoding:)`](https://developer.apple.com/documentation/foundation/nskeyedarchiver/2962880-archiveddata) replaces [`archivedData(withRootObject:)`](https://developer.apple.com/documentation/foundation/nskeyedarchiver/1413189-archiveddata) and [`archiveRootObject(_:toFile:)`](https://developer.apple.com/documentation/foundation/nskeyedarchiver/1410621-archiverootobject).
- [`init(forReadingFrom:)`](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/2962883-init) replaces [`init()`](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/2962882-init) and [`init(forReadingWith:)`](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/1410862-init).
- [`unarchivedObject(ofClass:from:)`](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/2983380-unarchivedobject) and [`unarchivedObject(ofClasses:from:)`](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/2962885-unarchivedobject) replace [`unarchiveObject(with:)`](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/1413894-unarchiveobject), [`unarchiveTopLevelObjectWithData(_:)`](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/2919664-unarchivetoplevelobjectwithdata), and [`unarchiveObject(withFile:)`](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/1417153-unarchiveobject). You use the new [`unarchivedObject(ofClasses:from:)`](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/2962885-unarchivedobject) method when unarchiving instances that are subclasses of one of the list of classes you supply. You can use these initializers and helper methods in apps that are compatible with macOS 10.13, iOS 11, watchOS 4, tvOS 11, and subsequent releases of each operating system.

For more information, see the WWDC 2018 session [`Data You Can Trust`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2018/222/).

##### Secure Value Transformer

[`NSSecureUnarchiveFromDataTransformer`](https://developer.apple.com/documentation/Foundation/NSSecureUnarchiveFromDataTransformer) is a new subclass of [`ValueTransformer`](https://developer.apple.com/documentation/Foundation/ValueTransformer). It uses [`NSKeyedArchiver`](https://developer.apple.com/documentation/Foundation/NSKeyedArchiver) and [`NSKeyedUnarchiver`](https://developer.apple.com/documentation/Foundation/NSKeyedUnarchiver) to archive and unarchive data by enabling doc://com.apple.documentation/documentation/Foundation/NSKeyedUnarchiver/1410824-requiresSecureCoding.

When unarchiving from [`NSData`](https://developer.apple.com/documentation/Foundation/NSData), [`NSSecureUnarchiveFromDataTransformer`](https://developer.apple.com/documentation/Foundation/NSSecureUnarchiveFromDataTransformer) uses its [`allowedTopLevelClasses`](https://developer.apple.com/documentation/foundation/nssecureunarchivefromdatatransformer/2962887-allowedtoplevelclasses) list to decode objects by calling the new [`unarchivedObject(ofClasses:from:)`](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/2962885-unarchivedobject) method. By default, this list includes all property list types—[`NSArray`](https://developer.apple.com/documentation/Foundation/NSArray), [`NSDictionary`](https://developer.apple.com/documentation/Foundation/NSDictionary), [`NSString`](https://developer.apple.com/documentation/Foundation/NSString), [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber), [`NSDate`](https://developer.apple.com/documentation/Foundation/NSDate), [`NSData`](https://developer.apple.com/documentation/Foundation/NSData), and [`NSNull`](https://developer.apple.com/documentation/Foundation/NSNull)—along with [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL) and [`NSUUID`](https://developer.apple.com/documentation/Foundation/NSUUID).

When archiving to [`NSData`](https://developer.apple.com/documentation/Foundation/NSData), this transformer calls the new [`archivedData(withRootObject:requiringSecureCoding:)`](https://developer.apple.com/documentation/foundation/nskeyedarchiver/2962880-archiveddata) method and enables requiresSecureCoding.

To transform top-level values of types other than the defaults listed above, subclass [`NSSecureUnarchiveFromDataTransformer`](https://developer.apple.com/documentation/Foundation/NSSecureUnarchiveFromDataTransformer).

- If you expect to decode a top-level value of only one allowed type, override [`transformedValueClass()`](https://developer.apple.com/documentation/foundation/valuetransformer/1401998-transformedvalueclass) to return that type. Doing so populates [`allowedTopLevelClasses`](https://developer.apple.com/documentation/foundation/nssecureunarchivefromdatatransformer/2962887-allowedtoplevelclasses) automatically.
- If you expect to decode a top-level value of one of several allowed types, override [`allowedTopLevelClasses`](https://developer.apple.com/documentation/foundation/nssecureunarchivefromdatatransformer/2962887-allowedtoplevelclasses) to return those types.

The older [`unarchiveFromDataTransformerName`](https://developer.apple.com/documentation/foundation/nsvaluetransformername/1402014-unarchivefromdatatransformername) and [`keyedUnarchiveFromDataTransformerName`](https://developer.apple.com/documentation/foundation/nsvaluetransformername/1402008-keyedunarchivefromdatatransforme) values are now deprecated.

##### Nssecurecoding Conformance

The [`NSPointerFunctions`](https://developer.apple.com/documentation/Foundation/NSPointerFunctions), [`NSMapTable`](https://developer.apple.com/documentation/Foundation/NSMapTable), and [`NSHashTable`](https://developer.apple.com/documentation/Foundation/nshashtable) classes now support limited conformance to the [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding) protocol. You can securely encode pointer-function consuming collections as long as you configure them with the following personalities and kinds of memory:

- [`objectPersonality`](https://developer.apple.com/documentation/foundation/nspointerfunctions/options/1411569-objectpersonality)
- [`objectPointerPersonality`](https://developer.apple.com/documentation/foundation/nspointerfunctions/options/1411202-objectpointerpersonality)
- [`strongMemory`](https://developer.apple.com/documentation/foundation/nspointerfunctions/options/1408849-strongmemory)
- [`weakMemory`](https://developer.apple.com/documentation/foundation/nspointerfunctions/options/1415896-weakmemory)
- [`copyIn`](https://developer.apple.com/documentation/foundation/nspointerfunctions/options/1413108-copyin) (optional)

> ❗ **Important**: Weak values won’t round-trip as expected unless you strongly reference them elsewhere during unarchival.

Weak values won’t round-trip as expected unless you strongly reference them elsewhere during unarchival.

##### Macro for Closed Enumerations

`NS_CLOSED_ENUM` is a new macro for declaring enumerations. You use it only for enumerations that are guaranteed to never gain an additional case. Usually you determine that there won’t be new cases because the enumeration you’re modeling represents a mathematically complete set. [`ComparisonResult`](https://developer.apple.com/documentation/Foundation/ComparisonResult) now adopts the `NS_CLOSED_ENUM` macro. It won’t ever gain additional cases.

> ❗ **Important**: Once an enumeration is marked as closed, it’s a binary- and source-incompatible change to add a new value. If you have any doubt about an enumeration gaining a private or additional public case in the future, use the `NS_ENUM` macro instead.

Once an enumeration is marked as closed, it’s a binary- and source-incompatible change to add a new value. If you have any doubt about an enumeration gaining a private or additional public case in the future, use the `NS_ENUM` macro instead.

For information about `NS_CLOSED_ENUM` and choosing between it and other macros for grouping constants, see [`Grouping Related Objective-C Constants`](https://developer.apple.com/documentation/Swift/grouping-related-objective-c-constants).

##### Userdefaults

[`UserDefaults`](https://developer.apple.com/documentation/Foundation/UserDefaults) has several bug fixes and improvements:

- Removed synchronization requirements. It’s no longer necessary to use [`synchronize()`](https://developer.apple.com/documentation/foundation/userdefaults/1414005-synchronize), [`CFPreferencesAppSynchronize(_:)`](https://developer.apple.com/documentation/CoreFoundation/CFPreferencesAppSynchronize(_:)), or [`CFPreferencesSynchronize(_:_:_:)`](https://developer.apple.com/documentation/CoreFoundation/CFPreferencesSynchronize(_:_:_:)). These methods will be deprecated in a future version of the OS.Now that you don’t need to call these synchronization methods, the performance characteristics of [`UserDefaults`](https://developer.apple.com/documentation/Foundation/UserDefaults) and Preferences Utilities are slightly different: The time taken for enqueueing write operations is now paid by the writing thread, rather than by the next thread to call [`synchronize()`](https://developer.apple.com/documentation/foundation/userdefaults/1414005-synchronize) or do a read operation.
- Removed retains when adding an observer. Adding observers to an instance of [`UserDefaults`](https://developer.apple.com/documentation/Foundation/UserDefaults) using the [`addObserver(_:forKeyPath:options:context:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/addObserver(_:forKeyPath:options:context:)) method unintentionally retained it, unlike all other uses of key-value observing. This has been corrected, and normal Cocoa memory management rules are now followed.
- Fixed key-value observing bug in [`UserDefaults`](https://developer.apple.com/documentation/Foundation/UserDefaults). Reading defaults on one thread while another thread set defaults could nondeterministically send key-value observing notifications on both threads, rather than just the thread doing the set operation. This is now fixed.

##### On Demand Resources

[`NSBundleResourceRequest`](https://developer.apple.com/documentation/Foundation/NSBundleResourceRequest) no longer throws exceptions when encountering certain kinds of internal errors. Instead, it returns an error in the error argument of the completion handler of the [`beginAccessingResources(completionHandler:)`](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/1614840-beginaccessingresources) method. The error might include the [`NSFileReadUnknownError`](https://developer.apple.com/documentation/foundation/nsfilereadunknownerror) and [`NSXPCConnectionInterrupted`](https://developer.apple.com/documentation/foundation/nsxpcconnectioninterrupted) errors in addition to [`NSUserCancelledError`](https://developer.apple.com/documentation/foundation/nsusercancellederror) and network-related errors.

If your app encounters an error when using [`NSBundleResourceRequest`](https://developer.apple.com/documentation/Foundation/NSBundleResourceRequest), request the resource again or display a prompt to your user to try again.

##### Thread Safety of Bundles

The [`principalClass`](https://developer.apple.com/documentation/foundation/bundle/1409048-principalclass) property on [`Bundle`](https://developer.apple.com/documentation/Foundation/Bundle) includes new thread-safety improvements. Accessing the property blocks if other threads are in the process of loading the bundle. This action allows the property to return the correct value in all cases.

##### Cfmessageport

The [`CFMessagePortSetName(_:_:)`](https://developer.apple.com/documentation/CoreFoundation/CFMessagePortSetName(_:_:)) function doesn’t do anything in apps linked on or after macOS 10.14, iOS 12, watchOS 5, and tvOS 12. This API will be deprecated in a future release.

In apps linked on earlier versions of macOS, iOS, watchOS, and tvOS, the [`CFMessagePortSetName(_:_:)`](https://developer.apple.com/documentation/CoreFoundation/CFMessagePortSetName(_:_:)) function doesn’t do anything if the message port already has a dispatch queue associated with itself via the [`CFMessagePortSetDispatchQueue(_:_:)`](https://developer.apple.com/documentation/CoreFoundation/CFMessagePortSetDispatchQueue(_:_:)) function. Previously, this pattern would result in undefined behavior.

In all cases, if you need to change the name of a [`CFMessagePort`](https://developer.apple.com/documentation/CoreFoundation/CFMessagePort), use [`CFMessagePortCreateLocal(_:_:_:_:_:)`](https://developer.apple.com/documentation/CoreFoundation/CFMessagePortCreateLocal(_:_:_:_:_:)) or [`CFMessagePortCreateRemote(_:_:)`](https://developer.apple.com/documentation/CoreFoundation/CFMessagePortCreateRemote(_:_:)).


---

*[View on Apple Developer](https://developer.apple.com/documentation/ios-ipados-release-notes/foundation-release-notes)*