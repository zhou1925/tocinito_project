import Image from 'next/image'
import { useRouter } from 'next/router';
import React from 'react'

const Sidebar = () => {

  const router = useRouter();

  return (
    <>
<div className="flex flex-col justify-between w-16 h-full bg-white border-r">

  <div>
    <a href="/" >
    <div className="inline-flex items-center justify-center w-16 h-16">
      {/* <Image src="/icons/llama.svg" height={50} width={50} /> */}
      <img  className={`opacity-50 ${router.route == "/" ? "opacity-100"  : "-50" } `} src="/icons/llama.svg" alt="Logo" />
      {/* <span className="block w-10 h-10 bg-gray-200 rounded-lg"></span> */}
    </div>
    </a>

    <div className="border-t border-gray-100">
      <nav className="flex flex-col p-2">
        <div className="py-4">
          <a
            href="/pos"
            className={`flex justify-center px-2 py-1.5 t text-blue-700 rounded group relative `}
          >
            <Image  className={`w-5 h-5 ${router.route == "/pos" ? "opacity-100 "  : "opacity-50" } `} src="/icons/fast_food.svg" height={70} width={70} />


            <span
              className="absolute text-xs font-medium text-white bg-gray-900 left-full ml-4 px-2 py-1.5 top-1/2 -translate-y-1/2 rounded opacity-0 group-hover:opacity-100"
            >
              Food
            </span>
          </a>
        </div>

        <ul className="pt-4 border-t border-gray-100 space-y-1">
          <li>
            <a
              href="/dashboard"
              className={`flex justify-center px-2 py-1.5 text-gray-500 rounded hover:bg-gray-50 hover:text-gray-700 relative group`}
            >
              <Image  className={` ${router.route == "/dashboard" ? "opacity-100 w-5 h-5 "  : "opacity-50" } `}  src="/icons/analytics.svg" height={70} width={70} />

              <span
                className="absolute text-xs font-medium text-white bg-gray-900 left-full ml-4 px-2 py-1.5 top-1/2 -translate-y-1/2 rounded opacity-0 group-hover:opacity-100"
              >
                Analytics
              </span>
            </a>
          </li>

          <li className="hidden">
            <a
              href=""
              className="flex relative group justify-center px-2 py-1.5 text-gray-500 rounded hover:bg-gray-50 hover:text-gray-700"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="w-5 h-5 opacity-75"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                stroke-width="2"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"
                />
              </svg>

              <span
                className="absolute text-xs font-medium text-white bg-gray-900 left-full ml-4 px-2 py-1.5 top-1/2 -translate-y-1/2 rounded opacity-0 group-hover:opacity-100"
              >
                Billing
              </span>
            </a>
          </li>

          <li className="hidden">
            <a
              href=""
              className="flex justify-center px-2 py-1.5 text-gray-500 rounded hover:bg-gray-50 hover:text-gray-700 relative group"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="w-5 h-5 opacity-75"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                stroke-width="2"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z"
                />
              </svg>

              <span
                className="absolute text-xs font-medium text-white bg-gray-900 left-full ml-4 px-2 py-1.5 top-1/2 -translate-y-1/2 rounded opacity-0 group-hover:opacity-100"
              >
                Invoices
              </span>
            </a>
          </li>

          <li className="hidden">
            <a
              href=""
              className="relative group flex justify-center px-2 py-1.5 text-gray-500 rounded hover:bg-gray-50 hover:text-gray-700"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="w-5 h-5 opacity-75"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                stroke-width="2"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
                />
              </svg>

              <span
                className="absolute text-xs font-medium text-white bg-gray-900 left-full ml-4 px-2 py-1.5 top-1/2 -translate-y-1/2 rounded opacity-0 group-hover:opacity-100"
              >
                Account
              </span>
            </a>
          </li>
        </ul>
      </nav>
    </div>
  </div>

  <div className="sticky inset-x-0 bottom-0 p-2 bg-white border-t border-gray-100 hidden">
    <form action="/logout">
      <button
        type="submit"
        className="flex justify-center w-full px-2 py-1.5 text-sm text-gray-500 rounded-lg hover:bg-gray-50 hover:text-gray-700 group relative"
      >
        <svg xmlns="http://www.w3.org/2000/svg" className="w-5 h-5 opacity-75" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"
          />
        </svg>

        <span
          className="absolute text-xs font-medium text-white bg-gray-900 left-full ml-4 px-2 py-1.5 top-1/2 -translate-y-1/2 rounded opacity-0 group-hover:opacity-100"
        >
          Logout
        </span>
      </button>
    </form>
  </div>
</div>

  
    </>
  )
}

export default Sidebar