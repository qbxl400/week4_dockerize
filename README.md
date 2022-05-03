
## Step by Step Instructions

#### Install git and clone this repo!
```
sudo apt install git
git clone https://github.com/qbxl400/week4_dockerize.git
```

#### Run it!
```
cd ..
cd week4_dockerize
docker build -t sentiment_image
docker run -d -p 8000:8000 sentiment_image
```

### Part 2: Deploying sentiment in the Cloud


#### Create account, setup billing, open terminal, upload files
```
cd week4_dockerize
gcloud builds submit --tag gcr.io/my-project/sentiment_image
gcloud run deploy --image gcr.io/my-project/sentiment_image --memory 4Gi
```

# License
All sources are free to use, but sentiment-analysis model is licensed under the MIT License.