# Defining file and data types for your app

**Framework**: Uniform Type Identifiers  
**Role**: Article

Declare uniform type identifiers to support your app’s proprietary data formats.

#### Overview

Apps that save, load, or transfer documents with proprietary data formats can define the file or data type for each format by:

1. Declaring your app’s custom type in the project’s `Info.plist` file.
2. Creating a new identifier for exported types, or using existing identifiers for imported types.
3. Defining each type’s conformance to system-declared types
4. Listing any associated file extensions or MIME types.

##### Declare a custom type for your app

When defining a type, you need to define it as an exported or imported type; this declaration indicates whether your app is the source of the type or whether it supports using a type defined elsewhere, respectively. If your app uses a type that this framework provides, don’t redeclare it in your app’s bundle.

Define an exported type when your app is the canonical source of information for that type. For example, if your app uses its own proprietary document format, declare it as an exported type.

Define an imported type if your app uses a type that another app defines, or if it’s a proprietary file format the system doesn’t declare. When importing a type from another app, don’t declare your own identifier; instead, use the same type identifier as the original.

##### Choose an identifier for your type

The identifiers you create for your app need to be unique. To ensure uniqueness, start by using a reverse DNS format that begins with `com.companyName`. Although the system supports different type identifier strings with the same specification, the reverse isn’t true. The identifier must contain only alphanumeric characters (`a–z`, `A`–`Z`, and `0`–`9`), hyphens (`-`), and periods (`.`). For example, you might use `com.example.greatAppDocument` or `com.example.greatApp-document` for the [`UTTypeIdentifier`](../BundleResources/information-property-list/utexportedtypedeclarations/uttypeidentifier.md) string in the `Info.plist` file.

> ❗ **Important**:  Don’t use `public`, `dyn`, or `com.apple` as the prefix in your app’s types. The system reserves `public` for public domain or standard types. The framework reserves the prefix `dyn` for types that it generates dynamically when no other type is available, and the prefix `com.apple` for types that Apple declares.

##### Define the conformance

The type declaration can include a list of type identifiers that the type conforms to. For example, if your app uses a proprietary file format based on `JSON`, use `public.json` in the [`UTTypeConformsTo`](../BundleResources/information-property-list/utexportedtypedeclarations/uttypeconformsto.md) string in the `Info.plist` file.

When defining a document type, make sure that it conforms to `public.data` or `com.apple.package` to ensure the Finder or Files app can represent it. If your type doesn’t conform to `public.data` or `com.apple.package`, the system can’t tell if a stored item has that type.

For document types, conform to `public.content`, either directly or by conforming to a type that already conforms to `public.content`. This conformance allows users to share your type over AirDrop.

You can also add conformance to functional types, such as `public.database` or `public.spreadsheet`. Conform your type to the most specific subtype applicable. Conforming to one or more functional types helps the system determine how best to display your app’s file types.

If you specify conformance to a nonpublic type, make sure that you also declare that type in your bundle.

##### Define the description, extensions, and MIME types

In addition to declaring the identifier, the type can define a user-readable string describing the type that you can also localize. For example, you might use `GreatApp Document` for the [`UTTypeDescription`](../BundleResources/information-property-list/utexportedtypedeclarations/uttypedescription.md) string in the `Info.plist` file.

Add a [`UTTypeTagSpecification`](../BundleResources/information-property-list/utexportedtypedeclarations/uttypetagspecification.md) dictionary in the `Info.plist` file to define the file extension or MIME types for your type. For example, add the string `greatappdoc` and `greatapp` into an array, and put it into the [`UTTypeTagSpecification`](../BundleResources/information-property-list/utexportedtypedeclarations/uttypetagspecification.md) dictionary with the key `public.filename-extension` to support both as file extensions for your type.

The following sample shows the exported example type added to an `Info.plist` file:

```plist
<key>UTExportedTypeDeclarations</key>
<array>
    <dict>
        <key>UTTypeIdentifier</key>
        <string>com.company.greatApp-document</string>
        <key>UTTypeConformsTo</key>
        <array>
            <string>public.json</string>
        </array>
        <key>UTTypeDescription</key>
        <string>GreatApp Document</string>
        <key>UTTypeTagSpecification</key>
        <dict>
            <key>public.filename-extension</key>
            <array>
                <string>greatappdoc</string>
                <string>greatapp</string>
            </array>
        </dict>
    </dict>
</array>
```

##### Specify the keys for declaring a type

The following table lists the available property keys that you use in type declarations:

| Key | Value type | Description |
| --- | --- | --- |
| [`UTExportedTypeDeclarations`](../BundleResources/information-property-list/utexportedtypedeclarations.md) | Array of dictionaries | An array of exported type declarations for identifiers your app owns. |
| [`UTImportedTypeDeclarations`](../BundleResources/information-property-list/utimportedtypedeclarations.md) | Array of dictionaries | An array of imported type declarations, typically types another company or organization declares. |
| [`UTTypeIdentifier`](../BundleResources/information-property-list/utexportedtypedeclarations/uttypeidentifier.md) | String | The identifier for the declared type. This key is required for type declarations. |
| [`UTTypeTagSpecification`](../BundleResources/information-property-list/utexportedtypedeclarations/uttypetagspecification.md) | Dictionary | A dictionary defining one or more equivalent type identifiers. |
| [`UTTypeConformsTo`](../BundleResources/information-property-list/utexportedtypedeclarations/uttypeconformsto.md) | Array of strings | The types the identifier conforms to. |
| [`UTTypeDescription`](../BundleResources/information-property-list/utexportedtypedeclarations/uttypedescription.md) | String | A user-visible description of the type. You can localize this string by including it in an `InfoPlist.strings` file. |
| [`UTTypeReferenceURL`](../BundleResources/information-property-list/utexportedtypedeclarations/uttypereferenceurl.md) | String | The URL of a reference document describing the type. |

If both exported and imported declarations for a type exist, the exported declaration takes precedence over the imported declaration.

## See Also

### Essentials
- [System-declared uniform type identifiers](./system-declared-uniform-type-identifiers.md)
  Common types that the system declares.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/defining-file-and-data-types-for-your-app)*