import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

predicate_pushdown="region in ('ca', 'gb', 'us')"

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1700069714841 = glueContext.create_dynamic_frame.from_catalog(
    database="og_de_youtube_raw",
    table_name="raw_statistics",
    transformation_ctx="AWSGlueDataCatalog_node1700069714841",
    push_down_predicate=predicate_pushdown
)

# Script generated for node Change Schema
ChangeSchema_node1700069736603 = ApplyMapping.apply(
    frame=AWSGlueDataCatalog_node1700069714841,
    mappings=[
        ("video_id", "string", "video_id", "string"),
        ("trending_date", "string", "trending_date", "string"),
        ("title", "string", "title", "string"),
        ("channel_title", "string", "channel_title", "string"),
        ("category_id", "long", "category_id", "long"),
        ("publish_time", "string", "publish_time", "string"),
        ("tags", "string", "tags", "string"),
        ("views", "long", "views", "long"),
        ("likes", "long", "likes", "long"),
        ("dislikes", "long", "dislikes", "long"),
        ("comment_count", "long", "comment_count", "long"),
        ("thumbnail_link", "string", "thumbnail_link", "string"),
        ("comments_disabled", "boolean", "comments_disabled", "boolean"),
        ("ratings_disabled", "boolean", "ratings_disabled", "boolean"),
        ("video_error_or_removed", "boolean", "video_error_or_removed", "boolean"),
        ("description", "string", "description", "string"),
        ("region", "string", "region", "string"),
    ],
    transformation_ctx="ChangeSchema_node1700069736603",
)

# Script generated for node Amazon S3
AmazonS3_node1700069841320 = glueContext.getSink(
    path="s3://og-de-on-youtube-cleansed-eucentral1-dev/youtube/raw_statistics/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=["region"],
    compression="snappy",
    enableUpdateCatalog=True,
    transformation_ctx="AmazonS3_node1700069841320",
)
AmazonS3_node1700069841320.setCatalogInfo(
    catalogDatabase="db_youtube_cleaned", catalogTableName="raw_statistics"
)
AmazonS3_node1700069841320.setFormat("glueparquet")
AmazonS3_node1700069841320.writeFrame(ChangeSchema_node1700069736603)
job.commit()
