import React from 'react'
import axios from 'axios';
import { useState, useEffect } from 'react';

const dashboard = () => {
    const [activeEvil, setActiveEvil] = useState(false);
  const [count, setCount] = useState(0);
  const [intervalId, setIntervalId] = useState(0);
  const [products, SetProducts] = useState({});

  let data = {};

  const getServerData = async () => {
    const res = await axios.get('https://tocinitov1.herokuapp.com/api/v1/orders/popular/');
    data = res.data;
    SetProducts(products => ({
      ...products,
      ...data
    }));

    // console.log(products);i
  }

  Object.keys(data).forEach((key) => {editor.write(`export const ${key}: "${data[key]}";\n`)
}

);

  const handleClick = () => {
    setActiveEvil(!activeEvil);
    if (intervalId) {
      clearInterval(intervalId);
      setIntervalId(0);
      return;
    }

    const newIntervalId = setInterval(() => {
      setCount(prevCount => prevCount + 1);
      getServerData();


    }, 10000);
    setIntervalId(newIntervalId);
  }

  useEffect(() => {
    console.log(activeEvil)
    if (activeEvil) {
      getServerData()
    }
    if (!activeEvil) {
      clearInterval()
    }
  }, [activeEvil])

  return (
    <div className="bg-gray-100">
      <div className="card w-96 text-neutral-content mx-auto">
        <div className="card-body items-center text-center">
          <div className="card-actions justify-evenly flex items-center">
          <p className="text-3xl"> {activeEvil ? '😈' : '😇'}</p>
          <input type="checkbox" className="toggle" onClick={handleClick}/>
          </div>
        </div>
      </div>

<div class="container flex flex-col mx-auto w-full items-center justify-center">
    <ul class="flex flex-col">

    {products &&
          Object.entries(products)
          .map( ([key, value]) => 

          <li class="border-gray-400 flex flex-row mb-2">
            <div class={`border select-none cursor-pointer bg-white rounded-xl flex flex-1 
            items-center p-4 shadow-xl transition duration-300 transform  hover:scale-75 ease-in-out hover:animate-pulse`}>
                
                <div class="flex flex-col w-10 h-10 justify-center items-center mr-4">
                    <span class={`font-semibold ${key === "0" ? "text-red-500" : ""}`}>{Number(key) + 1}</span>
                </div>
                <div class="flex-1 pl-1 md:mr-16">
                    <div class={`font-semibold ${key === "0" ? "text-red-500" : ""}`}>
                        {value}
                    </div>
                </div>
            </div>
        </li>
          )
    }
    </ul>
</div>

    </div>
  )
}

export default dashboard