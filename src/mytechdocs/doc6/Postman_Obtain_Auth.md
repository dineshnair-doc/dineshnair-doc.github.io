# Postman: Obtaining Authorization

This document explains how to use Postman to connect to the Spotify API. We'll walk through the process of obtaining authorization and making authenticated API requests to Spotify.

Spotify implements the OAuth 2.0 authorization framework. With OAuth 2.0, an application first retrieves an access token for the API, then uses that token to authenticate subsequent requests.

![Applications get the access token and then use that token for requests](diagram_accesstoken.png)

Let's see what happens when we send a request to Spotify without setting up authorization.

Step 1: Copy an endpoint from the [Spotify doc](https://developer.spotify.com/documentation/web-api).

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1732522558828/2304dd4f-1142-4561-afa9-e9c3489daf58.png align="center")

Step 2: Open the Postman desktop app, paste the endpoint for GET, and click **Send**.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1732522624172/940e7055-9530-4fce-b7d8-10d67041b683.png align="center")

When we click Send, we see a 401 Unauthorized error as the response. That means the request isn’t authorized to use Spotify API.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1732522777476/fc6eec10-9f7c-4d06-a26a-322497fba4a7.png align="center")

Let’s look at how to obtain authorization from Spotify.

### Create an App on Spotify

Step 1: Once you’ve signed up for a Spotify Developer account, go to the Dashboard and click **Create app**.

Step 2: Enter the app name and description.

Step 3: Enter redirect URL. This is the URL where users can be redirected after authentication. It’s also known as callback URL. As you’ll see later on, we’ll need to enter this URL in Postman as callback URL.

I’m using the Postman desktop app, so I entered the localhost URL for callback. If you’re using Postman online, refer to the authorization topic of the [Postman doc](https://learning.postman.com/) to find out the callback URL you should be using.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1732523003443/a0537168-9540-4277-aa39-5446a5de3ff9.png align="center")

Step 4: Click **Save**.

Step 5: After save, click **Settings** of the app to copy client ID and secret. We’ll use this ID and secret in Postman for configuring the authorization settings.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1732523058388/56d226db-5a93-4435-9dc9-ab46616cf941.png align="center")

### Configure Authorization Settings

Step 1: Open Postman. Create a new collection.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1732523179524/32e2ba21-7b0b-4eeb-8b63-974f74d58656.png align="center")

Step 2: Name the collection. For example, I named it *Spotify*.

Step 3: Click the **Authorization** tab and select *OAuth 2.0* as authorization type.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1732523244226/670aced0-8627-4ff5-9a68-57dc42c93060.png align="center")

Next, we’ll configure the new access token in the same **Authorization** tab.

Step 4: Leave the default value of grant type as *Authorization Code*.

Step 5: Enter callback URL as the same URL you entered in the Spotify app.

Step 6: Enter the Auth URL as `https://accounts.spotify.com/authorize`*.* This is the authorization server’s URL. You can find this URL in the [Spotify doc](https://developer.spotify.com/documentation/web-api).

Step 7: Enter the access token URL as `https://accounts.spotify.com/api/token`. You can find this URL in the [Spotify doc](https://developer.spotify.com/documentation/web-api).

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1732524658833/b0c42926-7ada-41a5-88e6-b41bb8d2f86e.png align="center")

Step 8: Enter your Spotify app’s client ID and secret. Postman suggests using variables to store these values to keep the sensitive data secure.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1732524732294/ce895185-213f-4040-ae6d-d84e656f99e0.png align="center")

Step 9: Enter the scope of values you’re requesting. For example, I entered *playlist-read-private playlist-modify-private.* You can find the list of acceptable scope values in the [Spotify doc](https://developer.spotify.com/documentation/web-api).

Step 10: Click **Save**.

Step 11: Scroll to the bottom of the page and click **Get New Access Token**.

Step 12: Spotify will ask you to sign in. After signing in, you’ll see the terms and conditions. Click **Agree** to proceed.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1732524817859/3e67c1b8-3c6d-46f7-a8e7-9eaab67b490d.png align="center")

Step 13: When you click **Agree**, a token is automatically generated. You can change the name of the token or use the default name. Click **Use Token** to set this token to be used for all requests in your collection.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1732524880503/36cc961c-5c4b-4ed2-801f-06e3bba5afad.png align="center")

### Send an API Request

Now that we’ve got the access token, let’s send a request.

Step 1: Copy the endpoint of a request from the [Spotify doc](https://developer.spotify.com/documentation/web-api). For this example, we’ll copy `https://api.spotify.com/v1/browse/new-releases`.

Step 2: Create a new request in the Spotify collection and paste the endpoint for GET.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1732525279974/80ac4daa-bd43-4adb-b7d0-06f9b6bbf66c.png align="center")

Step 3: Click **Send**.

Step 4: When you click Send, Postman displays the response from Spotify, indicating that the authorization setup is working.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1732525554540/6fe594b5-ed5c-4e8a-82ea-1a52925506be.png align="center")

You did it! You’ve now learned what happens when you send a request without authorization, how to configure authorization in Postman, and tested that your setup is working correctly.