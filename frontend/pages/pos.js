import axios from "axios";
import {useEffect, useState} from "react";
import Card from '../components/Card'
import Cart from '../components/Cart'
import Sidebar from '../components/Sidebar'

const dashboard = ({ data }) => {
  const { products, countProducts} = data;

  const [productsData, setProductsData] = useState(products);

  return (
    <div className="bg-white h-screen flex flex-wrap lg:flex-nowrap">

        <div className="xl:w-1/12 lg:w-1/12 md:w-1/12 xl:block sm:w-1/12 md:block hidden bg-gray-100">
            <Sidebar />
        </div>

        <div className="xl:w-8/12 lg:w-8/12 md:w-8/12 w-full overflow-visible bg-gray-100">
            <div className="grid grid-cols-1 xl:grid-cols-4 md:grid-cols-3 lg:grid-cols-3 gap-4 my-4 p-2 h-full max-h-screen overflow-y-auto">
                {productsData.map((product) => (
                    <Card key={product.slug} product={product}/>
                ))}
                {/* <Card /> */}

            </div>
        </div>

        <div className="xl:w-3/12 lg:w-3/12 md:w-3/12 hidden xl:block lg:block md:block w-full bg-gray-50">
            <Cart />
        </div>
    </div>
  )
}

export default dashboard

export async function getServerSideProps() {

    const res = await axios.get(`${process.env.API_BACKEND}orders/products/`);
    const data = res.data;
  
    return {
      props: {
        data,
      },
    };
  }