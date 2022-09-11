import React from 'react'
import { useStateContext } from '../lib/context';

const Card = ({ product }) => {
  const { title, price, image, slug } = product;
  const { qty, onAdd, setQty, cartItems } = useStateContext();
//   console.log(cartItems);

  const handleClick = () => {
    onAdd(product, qty);
  }

  return (
    <div >
        
        <div onClick={handleClick} 
        className="shadow-lg rounded-2xl hover:cursor-pointer
         p-4 bg-white w-64 h-64 relative xl:w-52 lg:w-52 
         md:w-40  m-auto md:h-62">
            
            <div className="w-full h-full text-center">
                <div className="flex h-full flex-col justify-between">
                    
                    <img className="object-cover rounded-lg h-32 md:h-28" src={` ${image === "" ? "/images/default_burger.jpg" : image}`}/>
                    <p className="text-gray-700 text-lg md:mt-2 font-bold mt-4">
                        {title}
                    </p>
                    <p className=" text-gray-700 text-md font-bold py-2 px-6 md:py-1 md:px-2">
                        S/{price}
                    </p>
                </div>
            </div>
        </div>


    </div>
  )
}

export default Card