function Product({productName, productPrice = 0, onclickfunction}){
    return (
        <div>
            <h2>Product name: {productName}</h2>
            <p>Product price: ${productPrice}</p>
            <button onClick={() => onclickfunction(productName)}>Buy Now</button>
        </div>
    )
}

export default Product;