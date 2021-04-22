import Link from 'next/link'
import {FaExclamationTriangle} from 'react-icons/fa'
import Layout from '@/components/Layout'
import styles from '@/styles/404.module.css'

const NotFound = () => {
  return (
    <Layout title='page not found'>
      <div className={styles.error}>
        <h1><FaExclamationTriangle />404</h1>
        <h4>Nothing available for you to see here</h4>
        <Link href='/'>Home</Link>
      </div>
    </Layout>
  )
}

export default NotFound
