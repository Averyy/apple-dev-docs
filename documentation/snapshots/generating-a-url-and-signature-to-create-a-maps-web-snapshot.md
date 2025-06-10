# Generating a URL and Signature to Create a Maps Web Snapshot

**Framework**: Maps Web Snapshots

Create a Snapshot URL and generate a signature to validate the request. 

#### Overview

You can use the Maps Web Snapshots service to retrieve static map images using a URL, in which you set the parameters that define the image. Begin by gathering your credentials, then create a snapshot URL using the parameters described in [`Create a Maps Web Snapshot`](create_a_maps_web_snapshot.md). Next, generate a signature by signing the URL string with your credentials. Finally, append the `signature` parameter to your Snapshot URL setting its value to the signature that you generated. You can also obtain HTML to show information about a place using [`Create a Map`](https://developer.apple.comhttp://developer.apple.com/maps/create-a-map/).

##### 3290796

All snapshot URLs must include a signature. To create your signature, gather the required credentials:

- Your Apple Developer Team ID
-  The Key ID for a key with the MapKit JS service enabled
-  Your private key file (.p8) for the key

If you don’t have a MapKit JS key, learn how to obtain one in [`Creating a Maps identifier and a private key`](https://developer.apple.com/documentation/applemapsserverapi/creating-a-maps-identifier-and-a-private-key).

> 💡 **Tip**: To locate your Team ID, sign in to your [`Apple Developer account`](https://developer.apple.comhttps://developer.apple.com/account) and click Membership in the left sidebar.

##### 3290639

Once you have your Team ID, Key ID, and private key file, use these credentials to generate a signature for a Maps Web Snapshots URL. You generate the signature using your credentials plus the snapshot URL request path and all query parameters, as described in [`Create a Maps Web Snapshot`](create_a_maps_web_snapshot.md). 

Using the query parameters to describe the characteristics of your map—such as its center, size, language, and so on—construct a snapshot URL. For example, this snapshot URL uses the `center` parameter to set the center point of the map image to Apple Park:

```other
https://snapshot.apple-mapkit.com/api/v1/snapshot?center=apple+park
```

> **Note**: Each query parameter must be URL-encoded. 

Add the `teamID` and `keyID` parameters to the URL, setting the values of the parameters to your own Team ID and Key ID. For example: 

```javascript
https://snapshot.apple-mapkit.com/api/v1/snapshot?center=apple+park&teamId=<your_team_id>&keyId=<your_key_id>
```

To generate a signature, sign the string with your private key using a ES256 algorithm (also known as ECDSA using P-256 curve and SHA-256 hash algorithm). The signature must be Base64 URL-encoded.

The generated signature allows you to access the exact request path and query parameters used in the signing process. If you modify or reorder the query parameters, you must generate a new signature.

##### 3290649

Append the `signature` parameter to your snapshots URL, and set the value of this parameter to the signature you generated. The `signature` parameter should always be the final parameter in a snapshots URL, as in this example:

```swift
https://snapshot.apple-mapkit.com/api/v1/snapshot?center=apple+park&teamId=<your_team_id>&keyId=<your_key_id>&signature=<your_generated_signature>
```

If the signature is the not the last query parameter, the request returns` 401 Authorization Error`.

##### 3314798

This example script uses JavaScript to do the following:

- Read the private key file from the file system.
- Define a `sign` function that creates a Snapshot URL and generates a signature for it. 
- Complete the Snapshots URL by appending the generated signature.
- Call the `sign` function to return a signed Snapshot URL for a simple map centered on Apple Park.

```javascript
// Required modules.
const { readFileSync } = require("fs");
const { sign } = require("jwa")("ES256");

/* Read your private key from the file system. (Never add your private key
 * in code or in source control. Always keep it secure.)
 */ 
const privateKey = readFileSync("[file_system_path]");
// Replace the team ID and key ID values with your actual values.
const teamId = "[team ID]";
const keyId = "[key ID]";

// Creates the signature string and returns the full Snapshot request URL including the signature.
function signRequest(params) {
    const snapshotPath = `/api/v1/snapshot?${params}`;
    const completePath = `${snapshotPath}&teamId=${teamId}&keyId=${keyId}`;
    const signature = sign(completePath, privateKey);
    // In this example, the jwa module returns the signature as a Base64 URL-encoded string.

    // Append the signature to the end of the request URL, and return.
    return `${completePath}&signature=${signature}`;
}

// Call the sign function with a simple map request.
signRequest("center=apple+park") 

// The return value expected is: "/api/v1/snapshot?center=apple+park&teamId=[team ID]&keyId=[key ID]&signature=[base64_url_encoded_signature]"
```

## See Also

- [object Annotation](annotation.md)
  An object for a Snapshot URL that describes annotation characteristics.
- [object Overlay](overlay.md)
  A JSON object for a Snapshot URL that describes overlay shape characteristics, including points for the overlay and styles such as width, color, and dash pattern.
- [object OverlayStyle](overlaystyle.md)
  A  JSON object that describes reusable styles for an overlay.
- [object Image](image.md)
  A JSON object for a Snapshot URL that describes the characteristics of custom images to use for map annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/snapshots/generating_a_url_and_signature_to_create_a_maps_web_snapshot)*