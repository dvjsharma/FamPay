from django.db import models

class Video(models.Model):
    """
    Model representing a video with relevant metadata.
    
    Attributes:
        video_id: Unique identifier for the video, serving as the primary key.
        title: Title of the video.
        description: Detailed description of the video content.
        publishedAt: Date and time when the video was published.
        thumbnail_url: URL of the video's thumbnail image.
        addedAt: Date and time when the video was added to the database.
    """

    video_id = models.CharField(max_length=11, primary_key=True)
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True)
    publishedAt = models.DateTimeField(null=False)
    thumbnail_url = models.URLField(null=True)
    addedAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Meta options for the Video model.
        """
        indexes = [
            models.Index(fields=['title']),    
            models.Index(fields=['description']),
            models.Index(fields=['publishedAt']),
        ]

    def __str__(self):
        """
        String representation of the Video model.
        """
        return self.title
