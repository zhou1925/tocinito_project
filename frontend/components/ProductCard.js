import Image from 'next/image';
import React from 'react'
import { useStateContext } from '../lib/context';

const ProductCard = ({ item }) => {
  const {  onRemove, onAdd } = useStateContext();


  return (
    <div className="flex items-start pb-2 pt-2">
        <img className="object-cover w-16 h-16 rounded-lg"
        src={` ${item.image === "" ? "/images/default_burger.jpg" : item.image}`}
        
      alt={`${item.title}`}
    />

    <div className="ml-4">
      <h3 className="text-sm font-semibold">{item.title}</h3>

      <dl className="mt-1 text-xs font-bold text-gray-800 space-y-1">
        <div>
          <dt className="inline">S/{item.price}</dt>
        </div>

        <div className="flex">
        <button className="inline text-lg font-bold w-8 bg-custom-yellow text-white rounded-md" onClick={() => onRemove(item)}>
            {/* <Image className="opacity-100 text-white" src="/icons/plus.svg" height={20} width={20} /> */}
            -
          </button>

          <p className="font-bold text-lg inline mx-4 lg:mx-2 sm:mx-1">{item.quantity}</p>

          <button className="inline text-lg font-bold w-8 bg-custom-yellow text-white rounded-md" onClick={() => onAdd(item, 1)}>
            {/* <Image className="opacity-100 fill-white" src="/icons/plus.svg" height={20} width={20} /> */}
            +
          </button>

        </div>
      </dl>
    </div>
    </div>
  )
}

export default ProductCard