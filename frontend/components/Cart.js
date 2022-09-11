import { useStateContext } from "../lib/context";
import axios from "axios";
import { useRouter } from 'next/router';
import { useState,useEffect } from "react";
import 'react-toastify/dist/ReactToastify.css';
import { toast } from 'react-toastify';
import ProductCard from './ProductCard'
import Image from "next/image";

const Cart = () => {

  const { cartItems, setShowCart, setTotalPrice, onAdd, setTotalQuantitites, onRemove, totalPrice, setCartItems } = useStateContext();
  const [checkoutLoader, setCheckoutLoader] = useState(false);

  const router = useRouter();

  const submitHandler = async (e) => {
    e.preventDefault();
    
    setCheckoutLoader(true);
    try {
      const res = await axios.post(
        `http://127.0.0.1:8000/api/v1/orders/create/`,
        { 'cart': JSON.stringify(cartItems),}
      );

      if (res.status === 200) {
        toast.success("Orden creada :)");
        setCartItems([]);
        setTotalQuantitites(0);
        setTotalPrice(0.0);
      }
    } catch (error) {
      toast.error("Ups algo salio mal :(");
    }
    

    setCheckoutLoader(false);
  }

  return (
    <>

    <div className=" px-2 py-4 max-h-screen overflow-y-auto block">
    {cartItems.length < 1 && (
      <div  className="flex flex-col justify-center items-center p-auto m-auto">
        <p className="text-gray-500 m-auto">No hay productos</p>
        <Image className="opacity-50 my-40" src="/icons/empty_cart.svg" height={100} width={100} />
      </div>
    )}
      {/* <div className="block max-w-sm px-0 py-4 sm:px-12 bg-stone-100 max-h-screen overflow-y-auto"> */}
      {cartItems.length >= 1 && (
        <span className="font-semibold text-gray-700">ORDEN</span>
      )}
      
    {cartItems.length >= 1 &&
            cartItems.map((item) => {
              return (
                <ProductCard key={item.slug} item={item}/>
              );
            })}

    {cartItems.length >= 1 && (
      <div>
              <h3 className="text-md my-2">Subtotal <span className="font-bold">S/{totalPrice}</span></h3>
            </div>
          )}
    {cartItems.length >= 1 && (
      
      <div className="text-center space-y-4">


      <button 
        onClick={submitHandler} 
        className={`block w-full p-3 text-sm rounded-lg
        ${checkoutLoader ? "cursor-not-allowed opacity-50" : ""}
        bg-custom-yellow text-custom-gray `} type="submit">
        {checkoutLoader ? "..." : "Guardar"}
      </button>

      </div>
    )}
</div>
    </>
  )
}

export default Cart