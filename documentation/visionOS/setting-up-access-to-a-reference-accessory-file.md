# Setting up access to a reference accessory file

**Framework**: visionOS

Track a generic spatial accessory by helping ARKit find the device’s reference accessory file.

#### Overview

To track a generic spatial accessory, your app needs a `.referenceaccessory` file that describes the device’s physical characteristics. ARKit uses the metadata in this file to recognize and track the device in physical space.

Manufacturers create `.referenceaccessory` files by training an accessory tracker model in Create ML. For more information on creating a reference accessory file, see [`Preparing spatial accessories for tracking in your visionOS app`](https://developer.apple.com/documentation/ARKit/preparing-spatial-accessories-for-tracking-in-your-visionos-app).

When your app initializes an [`Accessory`](https://developer.apple.com/documentation/ARKit/Accessory) from a connected [`GCSpatialAccessory`](https://developer.apple.com/documentation/GameController/GCSpatialAccessory), ARKit locates the corresponding `.referenceaccessory` file using a Uniform Type Identifier (UTI) registered with the system. If ARKit can’t find a matching file, initialization fails. For more information on Uniform Type Identifiers, see [`Defining file and data types for your app`](https://developer.apple.com/documentation/UniformTypeIdentifiers/defining-file-and-data-types-for-your-app).

This article covers the two ways to make a `.referenceaccessory` file available to your app: bundle the file with your app, or rely on ARKit to read it from the accessory manufacturer’s app when that app is also installed on the device.

#### Bundle the Reference Accessory File

Make sure you have the `.referenceaccessory` file for the generic spatial accessory you want to track. If you’re not the manufacturer, check with the device manufacturer to see whether they provide one. If they don’t, your app can instead rely on the manufacturer’s app to supply the file at runtime. For details, see [`Rely on the manufacturer’s app`](setting-up-access-to-a-reference-accessory-file#Rely-on-the-manufacturers-app.md).

To bundle the `.referenceaccessory` file, drag it into your Xcode project and select the checkbox next to your app target in the dialog that appears.

After bundling, declare the file type in your app’s `Info.plist` file. You can do this in Xcode’s property list editor or by editing the source directly. To use the property list editor:

1. In the Project navigator, select your app’s `Info.plist` file.
2. Hover over a row in the Information Property List and click the **+** button that appears.
3. If you’re the accessory manufacturer, choose “Exported Type Identifiers” from the dropdown. An exported declaration registers the type system-wide, so any other app installed on the device can also use the file as long as your app is present.
4. If you’re not the accessory manufacturer, choose “Imported Type Identifiers” instead. An imported declaration tells the system that your app depends on the type but doesn’t own it. If more than one app declares an imported type for the same identifier, the system picks one of them. If your app includes an imported declaration and the manufacturer’s app, with a matching exported declaration, is also installed, ARKit always gives the exported declaration precedence.
5. Expand the new entry’s “Item 0” and fill in the fields described below.

- ****Conforms to Type Identifiers** (`UTTypeConformsTo`)**: An array of parent types in the UTI conformance hierarchy. Set “Item 0” to the parent UTI. Check with the manufacturer for the correct value; `com.apple.spatial-device` is a reasonable default for spatial accessories.
- ****Identifier** (`UTTypeIdentifier`)**: The unique reverse-DNS identifier for this accessory type, provided by the manufacturer. Use the exact value of the `uniformTypeId` defined for the object class when training the `.referenceaccessory` file in Create ML.
- ****UTTypeReferenceAccessoryFile****: The exact filename of the `.referenceaccessory` file included in your app. Xcode shows this key under its raw name; type `UTTypeReferenceAccessoryFile` into the key field exactly as shown.
- ****Description** (`UTTypeDescription`)**: A human-readable name the system uses for display and debugging.

If you prefer editing `Info.plist` file’s source, use the exported declaration if you’re the manufacturer, or the imported declaration if you’re not:

**Exported**:

```xml
<key>UTExportedTypeDeclarations</key>
<array>
    <dict>
        <key>UTTypeConformsTo</key>
        <array>
            <!-- Standard parent type for spatial accessories. -->
            <string>com.apple.spatial-device</string>
        </array>
        <key>UTTypeIdentifier</key>
        <!-- The reverse-DNS identifier you defined for the accessory. -->
        <string>com.example.mycontroller</string>
        <key>UTTypeReferenceAccessoryFile</key>
        <!-- Filename of a `.referenceaccessory` bundled in your app's resources. -->
        <string>my_controller.referenceaccessory</string>
        <key>UTTypeDescription</key>
        <!-- Human-readable name. -->
        <string>My Controller</string>
    </dict>
</array>
```

**Imported**:

```xml
<key>UTImportedTypeDeclarations</key>
<array>
    <dict>
        <key>UTTypeConformsTo</key>
        <array>
            <!-- Confirm with the manufacturer. -->
            <string>com.apple.spatial-device</string>
        </array>
        <key>UTTypeIdentifier</key>
        <!-- Replace with the manufacturer's identifier. -->
        <string>com.example.mycontroller</string>
        <key>UTTypeReferenceAccessoryFile</key>
        <!-- Filename of a `.referenceaccessory` bundled in your app's resources. -->
        <string>my_controller.referenceaccessory</string>
        <key>UTTypeDescription</key>
        <!-- Human-readable name. -->
        <string>My Controller</string>
    </dict>
</array>
```

#### Rely on the Manufacturers App

If the manufacturer doesn’t make their `.referenceaccessory` file available for bundling, your app can instead rely on ARKit to find the file in the manufacturer’s app when that app is installed on the device. Your app doesn’t need any configuration changes for this path; just ensure your app handles initialization failures gracefully. When [`init(device:)`](https://developer.apple.com/documentation/ARKit/Accessory/init(device:)) throws, display an error with a button that helps the person install the manufacturer’s app.

```swift
do {
    let trackedAccessory = try await Accessory(device: accessory)
    // Use the tracked accessory.
} catch {
    logger.error("Failed to create accessory: \(error)")
    // Prompt the person to install the manufacturer's app.
}
```

For more information on prompting people to install another app, see [`SKOverlay`](https://developer.apple.com/documentation/StoreKit/SKOverlay) and [`appStoreOverlay(isPresented:configuration:)`](https://developer.apple.com/documentation/SwiftUI/View/appStoreOverlay(isPresented:configuration:)).

## See Also

- [Preparing spatial accessories for tracking in your visionOS app](../ARKit/preparing-spatial-accessories-for-tracking-in-your-visionos-app.md)
  Prepare a spatial accessory for tracking by training a reference accessory file and integrating it into your visionOS app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos/setting-up-access-to-a-reference-accessory-file)*