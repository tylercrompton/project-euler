import System.Environment

fib :: (Integral a) => a -> a
fib 0 = 0
fib 1 = 1
fib n = (fib (n - 2)) + (fib (n - 1))

p002 :: (Integral a) => a -> a
p002 n = sum (filter even (takeWhile (< n) (map fib [0..])))

main :: IO ()
main = do
	args <- getArgs
	putStrLn (show (p002 (read (head args) :: Int)))
