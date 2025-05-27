# Postman: Sending Requests
In the [previous document](../doc6/Postman_Obtain_Auth.md){target="_blank"}, we used Postman to complete the authorization process to gain access to the Spotify service and used the GET method to retrieve data. In this document, we'll extend our knowledge by examining the POST, PUT, and DELETE methods to interact with the Spotify service more comprehensively.

---

## Send a POST Request

Let's start with sending a POST request to create a playlist.

<span class="step-number">1</span> In the [Spotify doc](https://developer.spotify.com/documentation/web-api), go to the Create Playlist topic and copy the endpoint URL.

<span class="step-number">2</span> Open the Postman desktop app. We already created the *Spotify* collection in the previous tutorial. In the Spotify collection, add a new request.

![Add a new request option](post1.png)

<span class="step-number">3</span> Give a name to the request. For instance, *Create my playlist*.

<span class="step-number">4</span> Select POST and paste the endpoint URL you copied from the Spotify doc. You’ll need to replace `{user_id}` with the username from Spotify.

![Endpoint URL that mentions user ID](post2.png)

<span class="step-number">5</span> Go to your account in the [Spotify Web Player](https://open.spotify.com/), then click **Edit profile**, and copy the username value.

![username value](post3.png)

<span class="step-number">6</span> In Postman, replace the `{user_id}` value of the URL with the copied username. We can use a variable to store that username. Select the pasted username, then click **Set as variable**, and choose **Set as new variable**. Name the variable, for example, *username,* and set the scope of the variable as *Collection.* Finally, click **Set variable**. The endpoint will now have the variable in place of `{user_id}`.

![Username variable in the URL](post4.png)

<span class="step-number">7</span> The body of the POST request should contain the data to be created. In the [Spotify doc](https://developer.spotify.com/documentation/web-api), go to the Create Playlist topic, copy the request body. Note that in request body *false* means the playlist will be private.

![Doc request body](post5.png)

<span class="step-number">8</span> In Postman, click **Body**, and then **raw**. Paste the request body. I edited the copied request body to give a name to the playlist and a description.

![Post request body with playlist name](post6.png)

<span class="step-number">9</span> Click **Send**.

When you click send, you'll see *Status 201* appear. This status means the playlist was successfully created. Go ahead and copy the playlist ID from the response - we'll need it for the next step.

![Playlist ID in the response](post8.png)

You should now see your new playlist in your Spotify account as well.

![New playlist in Spotify account UI](post9.png)

Next, we'll add a couple of songs to the playlist.

<span class="step-number">1</span> In the [Spotify doc](https://developer.spotify.com/documentation/web-api), go to the Add Items to Playlist topic and copy the endpoint URL.

<span class="step-number">2</span> In the *Spotify* collection of Postman, add a new request. Name the request. For instance, *Add songs to my playlist*.

<span class="step-number">3</span> Select POST and paste the endpoint URL you copied from the Spotify doc.

<span class="step-number">4</span> In the endpoint URL, replace `{playlist_id}` with the ID of the playlist you just created. We'll use a variable like we used earlier for the username. Select the pasted playlist ID, then click **Set as variable**, followed by **Set as new variable**. Give the variable a name, for example, *playlistID*. Set the scope of the variable as *Collection* and click **Set variable**. The endpoint will now have the variable in place of `{playlist_id}`.

![playlistID in the endpoint URL](post10.png)

<span class="step-number">5</span> In the [Spotify doc](https://developer.spotify.com/documentation/web-api), go to the Add Items to Playlist topic and copy the example of the request body.

![Doc example of request body](post11.png)

<span class="step-number">6</span> In Postman, click **Body** and then **raw**. Then, paste the request body. I edited the copied request body to add two songs of my choice to the playlist.

![Request body with the two items to be added](post12.png)

You can find the track ID within the URL of the song on Spotify. For example, if the URL is `https://open.spotify.com/track/2va1fTXhffQcr6TfPGf16y`, the track ID would be `2va1fTXhffQcr6TfPGf16y`.

<span class="step-number">7</span> Click **Send**.

When you click send, you’ll see *Status 201* appear. This status means the songs were successfully added to the playlist. Spotify returns the snapshot ID of the playlist's current state.

![Snapshot ID of the playlist](post13.png)

You should now see the songs added to your playlist in your Spotify account as well.

## Send a PUT Request

We'll now use the PUT request to replace the two existing songs in the playlist with two new songs.

<span class="step-number">1</span> In the [Spotify doc](https://developer.spotify.com/documentation/web-api), go to the Update Playlist Items topic and copy the endpoint URL.

<span class="step-number">2</span> In the *Spotify* collection of Postman, add a new request. Give a name to the request. For instance, *Update my playlist*.

<span class="step-number">3</span> Select PUT and paste the endpoint URL you copied from the Spotify doc.

<span class="step-number">4</span> In the endpoint URL, replace `{playlist_id}` with the actual ID of the playlist. As we did previously for adding songs, we'll use the variable `playlistID`.

<span class="step-number">5</span> Copy the example of the URI array request body from the Spotify doc.

<span class="step-number">6</span> In Postman, click **Body**, and then **raw**. Then, paste the request body. I edited the request body to add the two songs of my choice to the playlist.

![Request body of the update endpoint](put1.png)

<span class="step-number">7</span> Click **Send**.

When you click send, you'll see *Status 200* appear. This status means the songs were successfully added to the playlist, replacing the earlier songs. Spotify returns the snapshot ID of the playlist's current state.

![Status 200 with snapshot ID of the playlist](put2.png)

You should now see your updated playlist in your Spotify account as well.

## Send a DELETE Request

Let's now use the DELETE request to delete a song from the playlist.

<span class="step-number">1</span> In the [Spotify doc](https://developer.spotify.com/documentation/web-api), go to the Remove Playlist Items topic and copy the endpoint URL.

<span class="step-number">2</span> In the *Spotify* collection of Postman, add a new request. Give a name to the request. For instance, *Delete from my playlist*.

<span class="step-number">3</span> Select DELETE and paste the endpoint URL you copied from the Spotify doc.

<span class="step-number">4</span> In the endpoint URL, replace `{playlist_id}` with the actual ID of the playlist. As we did previously for adding songs, we'll use the variable `playlistID`.

<span class="step-number">5</span> Copy the example of the URI array request body from the Spotify doc.

<span class="step-number">6</span> In Postman, click **Body**, and then **raw**. Then, paste the request body. I edited the request body to specify the one song that will be deleted from the playlist.

![Request body of delete endpoint](del1.png)

<span class="step-number">7</span> Click **Send**.

When you click send, you'll see *Status 200* appear. This status means the song was successfully deleted from the playlist. Spotify returns the snapshot ID of the playlist's current state.

![Status 200 that indicates successful deletion](del2.png)

You should now see your updated playlist in your Spotify account as well. The playlist will no longer include the song we just deleted.

In this document, we covered how to use POST, PUT, and DELETE requests with the Spotify API and Postman. We added songs to a playlist with a POST request, updated the playlist with new songs using a PUT request, and deleted a song with a DELETE request. By referencing the Spotify documentation, we learned how to construct our request bodies and understood the endpoints necessary for these operations. This hands-on experience should give you a good understanding of working with APIs.
