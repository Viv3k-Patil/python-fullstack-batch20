import Card from "./components/Card";
import Product from "./components/Product";

function App() {
  
  const products = [
    { id: 1, name: "Laptop", price: 50000 },
    { id: 2, name: "Mobile", price: 20000 },
    { id: 3, name: "Headphones", price: 2000 },
    { id: 4, name: "Laptop" },
    { id: 5, name: "Mobile", price: 20000 },
  ];

  function handleClick(product){
    console.log(`${product} is clicked`)
    alert(`${product} is clicked`)
  }

  const productsToRender = products.map((product) => (
    <Product 
      key={product.id}
      productName = {product.name}
      productPrice = {product.price}
      onclickfunction = {handleClick}
    />
  ))

  return (
    <>
      {productsToRender}
      <Card title="Special Offer" >This is information</Card>
    </>
  )
}

export default App