# Postman: Obtaining Authorization

This document explains how to use Postman to connect to the Spotify API. We'll walk through the process of obtaining authorization and making authenticated API requests to Spotify.

Spotify implements the OAuth 2.0 authorization framework. With OAuth 2.0, an application first retrieves an access token for the API, then uses that token to authenticate subsequent requests.

![Application gets the access token and then use that token for requests](diagram_accesstoken.png)

Let's see what happens when we send a request to Spotify without setting up authorization.

Step 1: Copy an endpoint from the [Spotify doc](https://developer.spotify.com/documentation/web-api).

![Endpoint URL](spotifydoc1.png)

Step 2: Open the Postman desktop app, paste the endpoint for GET, and click **Send**.

![Send button next to endpoint URL](wauth1.png)

When we click Send, we see a 401 Unauthorized error as the response. That means the request isn't authorized to use Spotify API.

![401 Unauthorized error message](wauth2.png)

Let's look at how to obtain authorization from Spotify.

## Create an App on Spotify

Step 1: Once you've signed up for a Spotify Developer account, go to the Dashboard and click **Create app**.

Step 2: Enter the app name and description.

Step 3: Enter redirect URL. This is the URL where users can be redirected after authentication. It's also known as callback URL. As you'll see later on, we'll need to enter this URL in Postman as callback URL.

I'm using the Postman desktop app, so I entered the localhost URL for callback. 

![Create app page with app name and callback URL](spotifyapp1.png)

If you're using Postman online, refer to the authorization topic of the [Postman doc](https://learning.postman.com/) to find out the callback URL you should be using.

Step 4: Click **Save**.

Step 5: After save, click **Settings** of the app to copy client ID and secret. We'll use this ID and secret in Postman for configuring the authorization settings.

![Client ID and secret](spotifyapp2.png)

## Configure Authorization Settings

Step 1: Open Postman. Create a new collection.

![Create collection](createauth1.png)

Step 2: Name the collection. For example, I named it *Spotify*.

Step 3: Click the **Authorization** tab and select *OAuth 2.0* as authorization type.

![OAuth 2.0 as authorization type](createauth2.png)

Next, we'll configure the new access token in the same **Authorization** tab.

Step 4: Leave the default value of grant type as *Authorization Code*.

Step 5: Enter callback URL as the same URL you entered in the Spotify app.

Step 6: Enter the Auth URL as `https://accounts.spotify.com/authorize`*.* This is the authorization server's URL. You can find this URL in the [Spotify doc](https://developer.spotify.com/documentation/web-api).

Step 7: Enter the access token URL as `https://accounts.spotify.com/api/token`. You can find this URL in the [Spotify doc](https://developer.spotify.com/documentation/web-api).

![Authorization tab with access token URL](createauth3.png)

Step 8: Enter your Spotify app's client ID and secret. Postman suggests using variables to store these values to keep the sensitive data secure.

![Set as variable option](createauth4.png)

Step 9: Enter the scope of values you're requesting. For example, I entered *playlist-read-private playlist-modify-private.* You can find the list of acceptable scope values in the [Spotify doc](https://developer.spotify.com/documentation/web-api).

Step 10: Click **Save**.

Step 11: Scroll to the bottom of the page and click **Get New Access Token**.

Step 12: Spotify will ask you to sign in. After signing in, you'll see the terms and conditions. Click **Agree** to proceed.

![Agree button and terms and conditions](createauth5.png)

Step 13: When you click **Agree**, a token is automatically generated. You can change the name of the token or use the default name. Click **Use Token** to set this token to be used for all requests in your collection.

![Access token displayed with the use token button near it](createauth6.png)

## Send an API Request

Now that we’ve got the access token, let’s send a request.

Step 1: Copy the endpoint of a request from the [Spotify doc](https://developer.spotify.com/documentation/web-api). For this example, we'll copy `https://api.spotify.com/v1/browse/new-releases`.

Step 2: Create a new request in the Spotify collection and paste the endpoint for GET.

![Endpoint and send button](sendreq1.png)

Step 3: Click **Send**.

Step 4: When you click Send, Postman displays the response from Spotify, indicating that the authorization setup is working.

![200 OK indicating a successful request and response from Spotify](sendreq2.png)

You did it! You've now learned how to configure authorization in Postman, and tested that your setup is working correctly.