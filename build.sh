#! /bin/bash
DATE=`date | sed 's/ /_/g' | sed 's/:/_/g'`
PRODUCT_NAME="PRODUCT_"
PRODUCT_FULL_NAME=${PRODUCT_NAME}${DATE}".tar.gz"
PRODUCT_FULL_NAME1=${PRODUCT_NAME}${DATE}".zip"


tar -zcvf ${PRODUCT_FULL_NAME} source/product.py build.sh execute.sh
zip -r ${PRODUCT_FULL_NAME1} source/product.py build.sh execute.sh
echo ${PRODUCT_FULL_NAME}
echo ${PRODUCT_FULL_NAME}

echo "Extracting...${PRODUCT_FULL_NAME}"

tar -zxvf ${PRODUCT_FULL_NAME}
unzip ${PRODUCT_FULL_NAME1}

