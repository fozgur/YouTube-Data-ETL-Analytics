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

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1698949095537 = glueContext.create_dynamic_frame.from_catalog(
    database="db_youtube_cleaned",
    table_name="cleaned_stat",
    transformation_ctx="AWSGlueDataCatalog_node1698949095537",
)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1698949201618 = glueContext.create_dynamic_frame.from_catalog(
    database="db_youtube_cleaned",
    table_name="youtube-csvparquetfirato_youtuberaw_parquets",
    transformation_ctx="AWSGlueDataCatalog_node1698949201618",
)

# Script generated for node Join
Join_node1698949245130 = Join.apply(
    frame1=AWSGlueDataCatalog_node1698949095537,
    frame2=AWSGlueDataCatalog_node1698949201618,
    keys1=["id"],
    keys2=["category_id"],
    transformation_ctx="Join_node1698949245130",
)

# Script generated for node Amazon S3
AmazonS3_node1698949322791 = glueContext.getSink(
    path="s3://youtube-analytical",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=["region", "category_id"],
    compression="snappy",
    enableUpdateCatalog=True,
    transformation_ctx="AmazonS3_node1698949322791",
)
AmazonS3_node1698949322791.setCatalogInfo(
    catalogDatabase="db_youtube_analytics", catalogTableName="final_analytic_data"
)
AmazonS3_node1698949322791.setFormat("glueparquet")
AmazonS3_node1698949322791.writeFrame(Join_node1698949245130)
job.commit()
