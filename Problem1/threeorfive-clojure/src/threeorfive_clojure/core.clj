(ns threeorfive-clojure.core
  (:gen-class))

(defn -main [& args]
  (def MAX_VALUE 1000)
  (println (reduce + (filter (fn [i]
    (or (= (mod i 3) 0) (= (mod i 5) 0))) (range MAX_VALUE)))))